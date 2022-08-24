import asyncio
from importlib import import_module

import orjson as json
import tornado.ioloop
import tornado.web
import tornado.websocket
from asgiref.sync import sync_to_async
from django.conf import settings
from django.contrib.auth import get_user
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from tornado.iostream import StreamClosedError

from routechoices.core.models import Event

EVENT_LIVE_DATA_STREAMS = {}


class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(tornado.escape.json_encode({"status": "ok"}))


class LiveEventDataHandler(tornado.web.RequestHandler):
    async def post(self, event_id):
        if (
            self.request.headers.get("Authorization")
            != f"Bearer {settings.LIVESTREAM_INTERNAL_SECRET}"
        ):
            raise tornado.web.HTTPError(403)
        try:
            data = json.loads(self.request.body)
        except Exception:
            raise tornado.web.HTTPError(400)
        ongoing_streams = EVENT_LIVE_DATA_STREAMS.get(event_id)
        if ongoing_streams:
            await asyncio.gather(
                *[stream.publish("locations", **data) for stream in ongoing_streams]
            )


class LiveEventDataStream(tornado.web.RequestHandler):
    def __init__(self, *args, **kwargs):
        self.listening = False
        return super().__init__(*args, **kwargs)

    def initialize(self):
        self.set_header(
            "Access-Control-Allow-Origin", self.request.headers.get("Origin", "*")
        )
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Methods", "GET")
        self.set_header("content-type", "text/event-stream")
        self.set_header("cache-control", "no-cache")

    async def get_current_user(self):
        engine = import_module(settings.SESSION_ENGINE)
        cookie = self.get_cookie(settings.SESSION_COOKIE_NAME)
        if not cookie:
            return None

        class Dummy:
            pass

        django_request = Dummy()
        django_request.session = engine.SessionStore(cookie)
        user = await sync_to_async(get_user)(django_request)
        return user

    async def publish(self, type_, **kwargs):
        if not self.listening:
            return
        try:
            jsonified = str(json.dumps({"type": type_, **kwargs}), "utf-8")
            self.write(f"data: {jsonified}\n\n".encode())
            await self.flush()
        except StreamClosedError:
            self.listening = False
            EVENT_LIVE_DATA_STREAMS[self.event_id].remove(self)
            if len(EVENT_LIVE_DATA_STREAMS[self.event_id]) == 0:
                EVENT_LIVE_DATA_STREAMS.pop(self.event_id, None)

    async def get(self, event_id):
        self.event_id = event_id
        event = await sync_to_async(
            Event.objects.select_related("club")
            .filter(
                aid=event_id,
                start_date__lte=now(),
                end_date__gte=now(),
            )
            .first,
            thread_sensitive=True,
        )()
        if not event:
            raise tornado.web.HTTPError(404)

        user = await self.get_current_user()
        if not user:
            raise tornado.web.HTTPError(403)
        if not user.is_superuser:
            if not user.is_authenticated:
                raise tornado.web.HTTPError(403)
            is_admin = await sync_to_async(
                event.club.admins.filter(id=user.id).exists, thread_sensitive=True
            )()
            if not is_admin:
                raise tornado.web.HTTPError(403)
        EVENT_LIVE_DATA_STREAMS.setdefault(event_id, [])
        EVENT_LIVE_DATA_STREAMS[event_id].append(self)
        self.listening = True
        while self.listening:
            await asyncio.sleep(5.0)
            await self.publish("ping")


class Command(BaseCommand):
    help = "Run SSE servers."

    def handle(self, *args, **options):
        live_data_tornado_app = tornado.web.Application(
            [
                (r"/health", HealthCheckHandler),
                (r"/([a-zA-Z0-9_-]{11})", LiveEventDataHandler),
                (r"/sse/([a-zA-Z0-9_-]{11})", LiveEventDataStream),
            ]
        )
        live_data_tornado_app.listen(8010)
        try:
            tornado.ioloop.IOLoop.instance().start()
        except KeyboardInterrupt:
            tornado.ioloop.IOLoop.current().stop()

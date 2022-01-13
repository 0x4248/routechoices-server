from django.core.management.base import BaseCommand

from routechoices.core.tasks import (
    import_single_event_from_tractrac,
    EventImportError,
)


class Command(BaseCommand):
    help = "Import race from tractrac.com"

    def add_arguments(self, parser):
        parser.add_argument("event_ids", nargs="+", type=str)
        parser.add_argument("--task", action="store_true", default=False)

    def handle(self, *args, **options):
        for event_id in options["event_ids"]:
            try:
                prefix = "https://live.tractrac.com/viewer/index.html?target="
                if event_id.startswith(prefix):
                    event_id = event_id[len(prefix) :]
                self.stdout.write(f"Importing event {event_id}")
                if options["task"]:
                    import_single_event_from_tractrac(event_id)
                else:
                    import_single_event_from_tractrac.now(event_id)
            except EventImportError:
                self.stderr.write(f"Could not import event {event_id}")
                continue

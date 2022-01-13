from django.core.management.base import BaseCommand

from routechoices.core.tasks import EventImportError, import_single_event_from_sportrec


class Command(BaseCommand):
    help = "Import race from sportrec.eu"

    def add_arguments(self, parser):
        parser.add_argument("event_ids", nargs="+", type=str)
        parser.add_argument("--task", action="store_true", default=False)

    def handle(self, *args, **options):
        for event_id in options["event_ids"]:
            try:
                prefix = "https://sportrec.eu/ui/#"
                if event_id.startswith(prefix):
                    event_id = event_id[len(prefix) :]
                self.stdout.write(f"Importing event {event_id}")
                if options["task"]:
                    import_single_event_from_sportrec(event_id)
                else:
                    import_single_event_from_sportrec.now(event_id)
            except EventImportError:
                self.stderr.write(f"Could not import event {event_id}")
                continue

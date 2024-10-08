from django.conf import settings
from django.core.management.base import BaseCommand

from routechoices.lib import s3


class Command(BaseCommand):
    help = "Create the storage bucket on the S3 storage"

    def handle(self, *args, **options):
        c = s3.get_s3_client()
        c.create_bucket(Bucket=settings.AWS_S3_BUCKET)

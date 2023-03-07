# Generated by Django 4.0.1 on 2022-01-18 12:23

import datetime
import re
import uuid
from datetime import timezone

import django.core.validators
import django.db.migrations.operations.special
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import routechoices.core.models
import routechoices.lib.helpers
import routechoices.lib.storages
import routechoices.lib.validators


def create_uuid(apps, schema_editor):
    pass


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# routechoices.core.migrations.0060_chatmessage_uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Club",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aid",
                    models.CharField(
                        default=routechoices.lib.helpers.random_key,
                        editable=False,
                        max_length=12,
                        unique=True,
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("modification_date", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "slug",
                    models.CharField(
                        help_text=".routechoices.com",
                        max_length=50,
                        unique=True,
                        validators=[routechoices.lib.validators.validate_domain_slug],
                    ),
                ),
                ("admins", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                (
                    "creator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default=(
                            "# GPS tracking powered by routechoices.com\n\n"
                            "Browse our events here."
                        ),
                        help_text=(
                            "This text will be displayed on your site frontpage, "
                            "use markdown formatting"
                        ),
                    ),
                ),
                (
                    "domain",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=128,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^([a-z0-9]+(-[a-z0-9]+)*\\.)+[a-z]{2,}$",
                                "Please enter a valid domain",
                            )
                        ],
                    ),
                ),
                ("acme_challenge", models.CharField(blank=True, max_length=128)),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        help_text="Image of size greater or equal than 128x128 pixels",
                        null=True,
                        storage=routechoices.lib.storages.OverwriteImageStorage(
                            aws_s3_bucket_name=settings.AWS_S3_BUCKET
                        ),
                        upload_to=routechoices.core.models.logo_upload_path,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "club",
                "verbose_name_plural": "clubs",
            },
        ),
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aid",
                    models.CharField(
                        default=routechoices.lib.helpers.short_random_key,
                        max_length=12,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                re.compile("^[-a-zA-Z0-9_]+\\Z"),
                                (
                                    "Enter a valid 'slug' consisting of letters, "
                                    "numbers, underscores or hyphens."
                                ),
                                "invalid",
                            )
                        ],
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(
                        auto_now_add=True, default=django.utils.timezone.now
                    ),
                ),
                ("is_gpx", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name_plural": "devices",
                "ordering": ["aid"],
                "verbose_name": "device",
            },
        ),
        migrations.CreateModel(
            name="Map",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aid",
                    models.CharField(
                        default=routechoices.lib.helpers.random_key,
                        editable=False,
                        max_length=12,
                        unique=True,
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("modification_date", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(
                        height_field="height",
                        max_length=255,
                        storage=routechoices.lib.storages.OverwriteImageStorage(
                            aws_s3_bucket_name=settings.AWS_S3_BUCKET
                        ),
                        upload_to=routechoices.core.models.map_upload_path,
                        width_field="width",
                    ),
                ),
                (
                    "height",
                    models.PositiveIntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "width",
                    models.PositiveIntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "corners_coordinates",
                    models.CharField(
                        help_text=(
                            "Latitude and longitude of map corners separated by commas "
                            "in following order "
                            "Top Left, Top right, Bottom Right, Bottom left. eg: "
                            "60.519,22.078,60.518,22.115,60.491,22.112,60.492,22.073"
                        ),
                        max_length=255,
                        validators=[
                            routechoices.lib.validators.validate_corners_coordinates
                        ],
                    ),
                ),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="maps",
                        to="core.club",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "maps",
                "ordering": ["-creation_date"],
                "verbose_name": "map",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aid",
                    models.CharField(
                        default=routechoices.lib.helpers.random_key,
                        editable=False,
                        max_length=12,
                        unique=True,
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("modification_date", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "slug",
                    models.CharField(
                        db_index=True,
                        help_text=(
                            "This the text that will be used in "
                            "the urls of your events"
                        ),
                        max_length=50,
                        validators=[routechoices.lib.validators.validate_nice_slug],
                    ),
                ),
                ("start_date", models.DateTimeField(verbose_name="Start Date (UTC)")),
                (
                    "map",
                    models.ForeignKey(
                        blank=True,
                        help_text="Pick a map from the club organizing",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="core.map",
                    ),
                ),
                (
                    "club",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="core.club",
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="End Date (UTC)"
                    ),
                ),
                (
                    "privacy",
                    models.CharField(
                        choices=[
                            ("public", "Public"),
                            ("secret", "Secret"),
                            ("private", "Private"),
                        ],
                        default="public",
                        max_length=8,
                        help_text=(
                            "Public: Listed on the front page | "
                            "Secret: Can be opened with a link, "
                            "however not listed on frontpage | "
                            "Private: Only a logged in admin of the club"
                            " can access the page"
                        ),
                    ),
                ),
                (
                    "open_registration",
                    models.BooleanField(
                        default=False,
                        help_text="Participants can register themselves to the event.",
                    ),
                ),
                (
                    "allow_route_upload",
                    models.BooleanField(
                        default=False,
                        help_text=(
                            "Participants can add their GPS trace "
                            "from a file after the event."
                        ),
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "events",
                "ordering": ["-start_date"],
                "verbose_name": "event",
                "unique_together": {("club", "slug")},
            },
        ),
        migrations.CreateModel(
            name="DeviceOwnership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ownerships",
                        to="core.device",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ownerships",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("device", "user")},
            },
        ),
        migrations.AddField(
            model_name="device",
            name="owners",
            field=models.ManyToManyField(
                related_name="devices",
                through="core.DeviceOwnership",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="locations_raw",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="device",
            name="aid",
            field=models.CharField(
                default=routechoices.lib.helpers.short_random_key,
                max_length=12,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^[-a-zA-Z0-9_]+\\Z"),
                        (
                            "Enter a valid “slug” consisting of letters, numbers, "
                            "underscores or hyphens."
                        ),
                        "invalid",
                    )
                ],
            ),
        ),
        migrations.CreateModel(
            name="ImeiDevice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "imei",
                    models.CharField(
                        max_length=32,
                        unique=True,
                        validators=[routechoices.lib.validators.validate_imei],
                    ),
                ),
                (
                    "device",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="physical_device",
                        to="core.device",
                    ),
                ),
            ],
            options={
                "verbose_name": "imei device",
                "verbose_name_plural": "imei devices",
                "ordering": ["imei"],
            },
        ),
        migrations.CreateModel(
            name="Competitor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aid",
                    models.CharField(
                        default=routechoices.lib.helpers.random_key,
                        editable=False,
                        max_length=12,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("short_name", models.CharField(default="X", max_length=32)),
                (
                    "start_time",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Start time (UTC)"
                    ),
                ),
                (
                    "device",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="competitor_set",
                        to="core.device",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="competitors",
                        to="core.event",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "competitors",
                "ordering": ["start_time", "name"],
                "verbose_name": "competitor",
            },
        ),
        migrations.CreateModel(
            name="MapAssignation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="map_assignations",
                        to="core.event",
                    ),
                ),
                (
                    "map",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="map_assignations",
                        to="core.map",
                    ),
                ),
            ],
            options={
                "unique_together": {("map", "event"), ("event", "title")},
                "ordering": ["id"],
            },
        ),
        migrations.AddField(
            model_name="event",
            name="extra_maps",
            field=models.ManyToManyField(
                related_name="_event_extra_maps_+",
                through="core.MapAssignation",
                to="core.Map",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="map",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="core.map",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="slug",
            field=models.CharField(
                db_index=True,
                help_text="This will be used in the url",
                max_length=50,
                validators=[routechoices.lib.validators.validate_nice_slug],
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="map_title",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Leave blank if you are not using extra maps",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="slug",
            field=models.CharField(
                db_index=True,
                default=routechoices.lib.helpers.short_random_slug,
                help_text="This is used to build the url of this event",
                max_length=50,
                validators=[routechoices.lib.validators.validate_nice_slug],
            ),
        ),
        migrations.CreateModel(
            name="Notice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("modification_date", models.DateTimeField(auto_now=True)),
                (
                    "text",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Optional text that will be displayed on the event page"
                        ),
                        max_length=280,
                    ),
                ),
                (
                    "event",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notice",
                        to="core.event",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2099, 12, 31, 23, 59, 59, 999, tzinfo=timezone.utc
                ),
                verbose_name="End Date (UTC) (*)",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(max_length=255, verbose_name="name (*)"),
        ),
        migrations.AlterField(
            model_name="event",
            name="slug",
            field=models.CharField(
                db_index=True,
                default=routechoices.lib.helpers.short_random_slug,
                help_text="This is used to build the url of this event",
                max_length=50,
                validators=[routechoices.lib.validators.validate_nice_slug],
                verbose_name="Slug (*)",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateTimeField(verbose_name="Start Date (UTC) (*)"),
        ),
        migrations.AlterField(
            model_name="event",
            name="club",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="core.club",
                verbose_name="Club (*)",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Name (*)"),
        ),
        migrations.AlterField(
            model_name="event",
            name="club",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="core.club",
                verbose_name="Club*",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(verbose_name="End Date (UTC)*"),
        ),
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Name*"),
        ),
        migrations.AlterField(
            model_name="event",
            name="slug",
            field=models.CharField(
                db_index=True,
                default=routechoices.lib.helpers.short_random_slug,
                help_text="This is used to build the url of this event",
                max_length=50,
                validators=[routechoices.lib.validators.validate_nice_slug],
                verbose_name="Slug*",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateTimeField(verbose_name="Start Date (UTC)*"),
        ),
        migrations.AlterField(
            model_name="event",
            name="club",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="core.club",
                verbose_name="Club",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="end_date",
            field=models.DateTimeField(verbose_name="End Date (UTC)"),
        ),
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(max_length=255, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="event",
            name="slug",
            field=models.CharField(
                db_index=True,
                default=routechoices.lib.helpers.short_random_slug,
                help_text="This is used to build the url of this event",
                max_length=50,
                validators=[routechoices.lib.validators.validate_nice_slug],
                verbose_name="Slug",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateTimeField(verbose_name="Start Date (UTC)"),
        ),
        migrations.AddField(
            model_name="device",
            name="modification_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="device",
            name="user_agent",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="event",
            name="backdrop_map",
            field=models.CharField(
                choices=[
                    ("blank", "Blank"),
                    ("osm", "Open Street Map"),
                    ("gmap-street", "Google Map Street"),
                    ("gmap-hybrid", "Google Map Satellite"),
                    ("mapant-fi", "Mapant Finland"),
                    ("mapant-no", "Mapant Norway"),
                    ("mapant-es", "Mapant Spain"),
                    ("topo-fi", "Topo Finland"),
                    ("topo-no", "Topo Norway"),
                ],
                default="blank",
                max_length=16,
            ),
        ),
        migrations.AlterModelOptions(
            name="event",
            options={
                "ordering": ["-start_date", "name"],
                "verbose_name": "event",
                "verbose_name_plural": "events",
            },
        ),
        migrations.CreateModel(
            name="SpotDevice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "messenger_id",
                    models.CharField(
                        max_length=32,
                        unique=True,
                        validators=[routechoices.lib.validators.validate_esn],
                    ),
                ),
                (
                    "device",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="spot_device",
                        to="core.device",
                    ),
                ),
            ],
            options={
                "verbose_name": "spot device",
                "verbose_name_plural": "spot devices",
                "ordering": ["messenger_id"],
            },
        ),
        migrations.CreateModel(
            name="SpotFeed",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("feed_id", models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name="device",
            name="aid",
            field=models.CharField(
                default=routechoices.lib.helpers.random_device_id,
                max_length=12,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^[-a-zA-Z0-9_]+\\Z"),
                        (
                            "Enter a valid “slug” consisting of letters, numbers, "
                            "underscores or hyphens."
                        ),
                        "invalid",
                    )
                ],
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="allow_live_chat",
            field=models.BooleanField(
                default=False,
                help_text="Spectator will have a chat enabled during the live.",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="backdrop_map",
            field=models.CharField(
                choices=[
                    ("blank", "Blank"),
                    ("osm", "Open Street Map"),
                    ("gmap-street", "Google Map Street"),
                    ("gmap-hybrid", "Google Map Satellite"),
                    ("mapant-fi", "Mapant Finland"),
                    ("mapant-no", "Mapant Norway"),
                    ("mapant-es", "Mapant Spain"),
                    ("topo-fi", "Topo Finland"),
                    ("topo-no", "Topo Norway"),
                    ("topo-world", "Topo World (OpenTopo)"),
                    ("topo-world-alt", "Topo World (ArcGIS)"),
                ],
                default="blank",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="extra_maps",
            field=models.ManyToManyField(
                related_name="+", through="core.MapAssignation", to="core.Map"
            ),
        ),
        migrations.CreateModel(
            name="ChatMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("ip_address", models.GenericIPAddressField()),
                ("nickname", models.CharField(max_length=20)),
                ("message", models.CharField(max_length=100)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chat_messages",
                        to="core.event",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, null=True),
                ),
            ],
            options={
                "ordering": ["-creation_date"],
                "verbose_name": "chat message",
                "verbose_name_plural": "chat messages",
            },
        ),
        migrations.RunPython(
            code=create_uuid,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="chatmessage",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name="club",
            name="description",
            field=models.TextField(
                blank=True,
                default=(
                    "# GPS tracking powered by routechoices.com\n\n"
                    "Browse our events here."
                ),
                help_text=(
                    "This text will be displayed on your site frontpage, "
                    "use markdown formatting"
                ),
            ),
        ),
        migrations.AddField(
            model_name="club",
            name="website",
            field=models.URLField(blank=True),
        ),
    ]

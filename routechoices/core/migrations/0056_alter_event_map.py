# Generated by Django 5.0a1 on 2023-09-26 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0055_alter_event_backdrop_map"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="map",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="events_main_map",
                to="core.map",
            ),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0018_alter_event_backdrop_map"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="analytics_site",
            field=models.URLField(blank=True, max_length=256),
        ),
    ]

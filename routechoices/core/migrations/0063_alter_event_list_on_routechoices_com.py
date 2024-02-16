# Generated by Django 5.0.1 on 2024-02-16 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0062_club_forbid_invite_request"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="list_on_routechoices_com",
            field=models.BooleanField(
                default=False, verbose_name="Listed on Routechoices.com events page"
            ),
        ),
    ]

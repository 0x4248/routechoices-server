# Generated by Django 3.2.5 on 2021-08-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0043_club_domain"),
    ]

    operations = [
        migrations.AddField(
            model_name="club",
            name="acme_challenge",
            field=models.CharField(blank=True, max_length=128),
        ),
    ]

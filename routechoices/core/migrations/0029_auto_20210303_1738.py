# Generated by Django 3.1.4 on 2021-03-03 17:38

from django.db import migrations, models
import routechoices.lib.helpers
import routechoices.lib.validators


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0028_auto_20210211_1003"),
    ]

    operations = [
        migrations.AlterField(
            model_name="club",
            name="slug",
            field=models.CharField(
                help_text="This is used in the urls of your events",
                max_length=50,
                unique=True,
                validators=[routechoices.lib.validators.validate_nice_slug],
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
    ]

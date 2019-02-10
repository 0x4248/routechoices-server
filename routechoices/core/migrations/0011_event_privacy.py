# Generated by Django 2.1.5 on 2019-02-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190205_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='privacy',
            field=models.CharField(choices=[('public', 'Public'), ('secret', 'Secret'), ('private', 'Private')], default='public', max_length=8),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-23 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200223_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name_full_fromatted',
            new_name='name_full_formatted',
        ),
    ]
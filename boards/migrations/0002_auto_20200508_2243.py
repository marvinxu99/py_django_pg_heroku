# Generated by Django 3.0.4 on 2020-05-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='description',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
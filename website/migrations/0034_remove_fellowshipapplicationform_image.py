# Generated by Django 3.0.5 on 2020-05-29 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_fellowshipapplicationform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fellowshipapplicationform',
            name='image',
        ),
    ]
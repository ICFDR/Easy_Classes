# Generated by Django 3.0.5 on 2020-05-11 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_remove_donate_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Programs',
            new_name='Campaign',
        ),
        migrations.AlterModelOptions(
            name='campaign',
            options={'verbose_name_plural': 'Campaigns'},
        ),
    ]
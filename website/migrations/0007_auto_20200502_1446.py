# Generated by Django 3.0.5 on 2020-05-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_aboutus'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardteam',
            name='image_alt_txt',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='leadersays',
            name='image_alt_txt',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ourcauses',
            name='image_alt_txt',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ourchildrens',
            name='image_alt_txt',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

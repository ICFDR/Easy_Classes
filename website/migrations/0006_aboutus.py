# Generated by Django 3.0.5 on 2020-05-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200428_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
    ]

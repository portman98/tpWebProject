# Generated by Django 2.0.3 on 2018-04-13 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qSite', '0012_auto_20180412_1950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-rating']},
        ),
    ]

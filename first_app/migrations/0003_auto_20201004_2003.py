# Generated by Django 3.0.3 on 2020-10-04 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20201004_1954'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loaddataproces',
            old_name='fileName',
            new_name='eeg',
        ),
    ]
# Generated by Django 3.0.3 on 2020-10-12 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20201004_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='EDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edf_name', models.CharField(blank=True, max_length=100, null=True)),
                ('row_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
    ]

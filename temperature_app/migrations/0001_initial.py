# Generated by Django 4.2.7 on 2023-11-20 13:49

from django.db import migrations, models
import django.utils.timezone
import timescale.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemperatureReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', timescale.db.models.fields.TimescaleDateTimeField(default=django.utils.timezone.now, interval='1 day')),
                ('temperature', models.FloatField()),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
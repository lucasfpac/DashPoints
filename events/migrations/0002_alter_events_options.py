# Generated by Django 4.2.16 on 2024-09-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]

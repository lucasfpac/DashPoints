# Generated by Django 4.2.16 on 2024-09-25 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('purchases', '0005_alter_purchases_options_remove_purchases_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='Events',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='events.events'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_room_room_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]
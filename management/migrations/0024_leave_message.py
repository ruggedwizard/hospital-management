# Generated by Django 4.0.3 on 2022-08-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0023_alter_appointment_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='nullprovided@gmail.com', max_length=254)),
                ('message_for_doctor', models.CharField(max_length=5000)),
                ('date_of_complaint', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0018_alter_doctor_doctor_user_instance'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Profile_image',
            field=models.ImageField(default='Null', upload_to='management/image'),
        ),
    ]

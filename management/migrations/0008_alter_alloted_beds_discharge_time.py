# Generated by Django 4.0 on 2022-04-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_alter_alloted_beds_discharge_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alloted_beds',
            name='Discharge_time',
            field=models.DateField(blank=True, default='00-00-00'),
        ),
    ]

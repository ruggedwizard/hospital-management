# Generated by Django 4.0.3 on 2022-04-10 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_bill_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='Department_details',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
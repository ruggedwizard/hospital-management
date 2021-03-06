# Generated by Django 4.0.3 on 2022-04-16 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_donors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=2048, null=True)),
                ('date', models.DateTimeField()),
                ('emergency', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.doctor')),
                ('patient', models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Birth_report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=2048, null=True)),
                ('mode_of_delivery', models.CharField(blank=True, max_length=250, null=True)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
            ],
        ),
    ]

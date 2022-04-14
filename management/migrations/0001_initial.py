# Generated by Django 4.0 on 2022-04-14 20:11

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=250)),
                ('Contact_email', models.EmailField(blank=True, default='notprovided@example.com', max_length=500, null=True)),
                ('Contact_phone', models.CharField(max_length=250)),
                ('Appointment_date', models.DateTimeField()),
                ('Reason_for_Appointment', models.TextField(max_length=2500)),
                ('Appointment_completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
            options={
                'ordering': ['Appointment_date'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_name', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('Department_details', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_location', models.CharField(blank=True, max_length=250, null=True)),
                ('Room_ID', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('Room_availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_lastname', models.CharField(blank=True, max_length=250, null=True)),
                ('Patient_firstname', models.CharField(blank=True, max_length=250, null=True)),
                ('Patient_phone_number', models.CharField(blank=True, max_length=120, null=True)),
                ('Patient_address', models.CharField(blank=True, max_length=350, null=True)),
                ('Patient_age', models.IntegerField(blank=True, null=True)),
                ('Patient_gender', models.CharField(choices=[('UNDECIDED', 'UNDECIDED'), ('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='UNDECIDED', max_length=25)),
                ('Patient_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.CharField, to='management.room')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor_firstname', models.CharField(blank=True, max_length=250, null=True)),
                ('Doctor_lastname', models.CharField(blank=True, max_length=250, null=True)),
                ('Doctor_gender', models.CharField(choices=[('UNDECIDED', 'UNDECIDED'), ('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='UNDECIDED', max_length=25)),
                ('Doctor_specialization', models.CharField(blank=True, max_length=250, null=True)),
                ('Doctor_phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('Doctor_email_address', models.EmailField(blank=True, default='firstname.lastname@hospitalmanagement.com', max_length=254, null=True)),
                ('Doctor_location', models.CharField(blank=True, max_length=250, null=True)),
                ('Doctor_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_department', to='management.department')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.FloatField(max_length=2000)),
                ('payment_status', models.CharField(choices=[('PENDING', 'PENDING'), ('COMPLETED', 'COMPLETED')], default='PENDING', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.patient')),
            ],
        ),
    ]

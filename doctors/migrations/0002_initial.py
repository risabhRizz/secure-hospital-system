# Generated by Django 4.0.1 on 2022-03-12 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('hospital_staffs', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='patientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patientprofile'),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='staffId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_staffs.hospitalstaffprofile'),
        ),
    ]

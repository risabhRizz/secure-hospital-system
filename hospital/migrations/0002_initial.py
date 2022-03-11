# Generated by Django 4.0.1 on 2022-03-11 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('hospital', '0001_initial'),
        ('hospital_staffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patientprofile'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='staffId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_staffs.hospitalstaffprofile'),
        ),
    ]

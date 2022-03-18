# Generated by Django 4.0.1 on 2022-03-18 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0002_initial'),
        ('insurance_staffs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital_staffs', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancestaffprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='patientId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patientprofile'),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='staffId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_staffs.hospitalstaffprofile'),
        ),
        migrations.AddField(
            model_name='insuranceclaim',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.0.1 on 2022-03-16 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lab_staffs', '0001_initial'),
        ('hospital_staffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics')),
                ('address', models.CharField(blank=True, max_length=70, null=True)),
                ('insurance', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30, null=True)),
                ('transactionAmount', models.DecimalField(decimal_places=4, max_digits=6, null=True)),
                ('patientID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patientprofile')),
                ('staffId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_staffs.hospitalstaffprofile')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.CreateModel(
            name='PatientRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.TextField(null=True)),
                ('prescription', models.TextField(null=True)),
                ('doctorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital_staffs.hospitalstaffprofile')),
                ('labTestId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab_staffs.labstaffprofile')),
                ('patientID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patientprofile')),
            ],
            options={
                'db_table': 'patientrecords',
            },
        ),
    ]

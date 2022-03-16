<<<<<<< Updated upstream
<<<<<<< Updated upstream
# Generated by Django 4.0.1 on 2022-02-25 03:36
=======
# Generated by Django 4.0.1 on 2022-03-11 20:40
>>>>>>> Stashed changes
=======
# Generated by Django 4.0.1 on 2022-03-11 22:21
>>>>>>> Stashed changes

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< Updated upstream
<<<<<<< Updated upstream
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_type', models.CharField(choices=[('hospital_staff', 'Hospital Staff'), ('doctor', 'Doctor'), ('insurance_staff', 'Insurance Staff'), ('lab_staff', 'Lab Staff'), ('administrators', 'Administrators')], default='hospital_staff', max_length=20)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=20, null=True)),
            ],
=======
            name='AdministratorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
=======
            name='AdministratorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
>>>>>>> Stashed changes
        ),
        migrations.CreateModel(
            name='Deleted_Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('employee_type', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_type', models.CharField(choices=[('hospital_staff', 'Hospital Staff'), ('doctor', 'Doctor'), ('insurance_staff', 'Insurance Staff'), ('lab_staff', 'Lab Staff'), ('administrators', 'Administrators')], default='hospital_staff', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
        ),
    ]

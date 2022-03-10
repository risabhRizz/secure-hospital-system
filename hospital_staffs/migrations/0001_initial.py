# Generated by Django 4.0.1 on 2022-03-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalStaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=70, null=True)),
                ('role', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'staff',
            },
        ),
    ]
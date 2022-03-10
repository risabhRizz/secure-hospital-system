# Generated by Django 4.0.1 on 2022-03-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insuranceClaim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claimAmount', models.DecimalField(decimal_places=4, max_digits=6, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('testResult', models.TextField(null=True)),
            ],
            options={
                'db_table': 'insuranceclaim',
            },
        ),
        migrations.CreateModel(
            name='InsuranceStaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
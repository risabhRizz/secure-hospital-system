# Generated by Django 4.0.1 on 2022-02-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrators', '0004_employee_first_name_employee_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='password',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

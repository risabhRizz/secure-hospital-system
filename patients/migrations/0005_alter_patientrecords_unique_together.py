# Generated by Django 4.0.1 on 2022-03-17 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_patientrecords_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='patientrecords',
            unique_together=set(),
        ),
    ]

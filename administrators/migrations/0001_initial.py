# Generated by Django 4.0.1 on 2022-03-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logDetails', models.TextField(null=True)),
            ],
            options={
                'db_table': 'logs',
            },
        ),
    ]

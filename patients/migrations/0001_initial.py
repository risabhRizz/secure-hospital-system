# Generated by Django 4.0.1 on 2022-02-15 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_user_is_admin_remove_user_is_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

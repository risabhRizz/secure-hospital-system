<<<<<<< Updated upstream
# Generated by Django 4.0.1 on 2022-02-25 03:36
=======
# Generated by Django 4.0.1 on 2022-03-11 20:40
>>>>>>> Stashed changes

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< Updated upstream
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
        ('patients', '0001_initial'),
>>>>>>> Stashed changes
        ('lab_staffs', '0001_initial'),
        ('hospital_staffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labstaffprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

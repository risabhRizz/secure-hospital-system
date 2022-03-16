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
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='patients.patientprofile')),
                ('scheduled_date', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-scheduled_date', '-created'],
            },
        ),
    ]

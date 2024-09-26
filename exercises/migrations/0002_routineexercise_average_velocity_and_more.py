# Generated by Django 4.2.15 on 2024-09-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='routineexercise',
            name='average_velocity',
            field=models.FloatField(blank=True, help_text='Average velocity in km/h for cardio exercises', null=True),
        ),
        migrations.AddField(
            model_name='routineexercise',
            name='day_of_week',
            field=models.CharField(blank=True, choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='routineexercise',
            name='distance',
            field=models.FloatField(blank=True, help_text='Distance in kilometers for cardio exercises', null=True),
        ),
        migrations.AddField(
            model_name='routineexercise',
            name='duration',
            field=models.PositiveIntegerField(blank=True, help_text='Duration in minutes for cardio exercises', null=True),
        ),
        migrations.AddField(
            model_name='routineexercise',
            name='pace',
            field=models.FloatField(blank=True, help_text='Pace in minutes per kilometer for cardio exercises', null=True),
        ),
    ]

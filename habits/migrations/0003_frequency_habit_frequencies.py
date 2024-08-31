# Generated by Django 4.2.15 on 2024-08-31 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_habit_measure'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=8, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='habit',
            name='frequencies',
            field=models.ManyToManyField(to='habits.frequency'),
        ),
    ]

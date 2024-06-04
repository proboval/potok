# Generated by Django 5.0.6 on 2024-06-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threadPrediction', '0002_alter_mrimask_headmri'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='doctor',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='expert',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='research',
            field=models.ManyToManyField(blank=True, to='threadPrediction.research'),
        ),
    ]
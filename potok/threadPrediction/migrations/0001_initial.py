# Generated by Django 5.0.6 on 2024-06-01 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadMRI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='images/MRI/')),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MRIMask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='images/Masks/')),
                ('headMRI', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Mask', to='threadPrediction.headmri')),
            ],
        ),
        migrations.AddField(
            model_name='headmri',
            name='research',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MRIs', to='threadPrediction.research'),
        ),
    ]

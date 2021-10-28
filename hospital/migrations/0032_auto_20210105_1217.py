# Generated by Django 3.1.5 on 2021-01-05 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0031_auto_20210105_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]

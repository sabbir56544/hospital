# Generated by Django 3.1.4 on 2021-01-02 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_patient_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='time',
            field=models.CharField(max_length=25),
        ),
    ]
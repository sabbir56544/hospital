# Generated by Django 3.1.5 on 2021-01-05 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0030_unique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Unique',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='entry_date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.AddField(
            model_name='appointment',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='phone',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='symptoms',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]

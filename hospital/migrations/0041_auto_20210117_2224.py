# Generated by Django 3.1.1 on 2021-01-17 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0040_remove_appointment_is_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_appointment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appointment',
            name='symptoms_details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

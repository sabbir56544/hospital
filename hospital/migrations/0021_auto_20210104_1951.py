# Generated by Django 3.1.4 on 2021-01-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='entry_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='room_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='room_service',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

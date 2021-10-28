# Generated by Django 3.1.4 on 2021-01-02 18:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_auto_20210103_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='appointment_time',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='created_at_date',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='created_at_time',
        ),
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 1, 2, 18, 21, 39, 167800, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='appointment_date',
            field=models.DateTimeField(null=True),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-02 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_auto_20210103_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]

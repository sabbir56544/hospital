# Generated by Django 3.1.4 on 2021-01-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0017_auto_20210103_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='appointment_date',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-02 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_auto_20210103_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='time',
        ),
    ]
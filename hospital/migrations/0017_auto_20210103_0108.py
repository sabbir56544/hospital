# Generated by Django 3.1.4 on 2021-01-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_appoi'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appoi',
        ),
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

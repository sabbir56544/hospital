# Generated by Django 3.1.4 on 2021-01-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20210102_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]

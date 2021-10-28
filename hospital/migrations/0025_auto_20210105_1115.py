# Generated by Django 3.1.1 on 2021-01-05 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0024_auto_20210104_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='room_no',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='room_service',
        ),
        migrations.RemoveField(
            model_name='patientdischarge',
            name='appointment',
        ),
        migrations.CreateModel(
            name='Admitted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('room_no', models.IntegerField()),
                ('room_service', models.IntegerField()),
                ('admited_date', models.DateField(null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
            ],
        ),
        migrations.AddField(
            model_name='patientdischarge',
            name='admitted',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.admitted'),
        ),
    ]
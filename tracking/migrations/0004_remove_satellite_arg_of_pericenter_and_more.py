# Generated by Django 4.2 on 2024-05-05 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_satellite_launch_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='satellite',
            name='arg_of_pericenter',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='bstar',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='classification_type',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='eccentricity',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='element_set_no',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='ephemeris_type',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='epoch',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='inclination',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='launch_country',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='mean_anomaly',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='mean_motion',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='mean_motion_ddot',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='mean_motion_dot',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='norad_cat_id',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='ra_of_asc_node',
        ),
        migrations.RemoveField(
            model_name='satellite',
            name='rev_at_epoch',
        ),
        migrations.AlterField(
            model_name='satellite',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='SatelliteHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epoch', models.DateTimeField()),
                ('mean_motion', models.FloatField()),
                ('eccentricity', models.FloatField()),
                ('inclination', models.FloatField()),
                ('ra_of_asc_node', models.FloatField()),
                ('arg_of_pericenter', models.FloatField()),
                ('mean_anomaly', models.FloatField()),
                ('ephemeris_type', models.IntegerField()),
                ('classification_type', models.CharField(max_length=1)),
                ('norad_cat_id', models.IntegerField(unique=True)),
                ('element_set_no', models.IntegerField()),
                ('rev_at_epoch', models.IntegerField()),
                ('bstar', models.FloatField()),
                ('mean_motion_dot', models.FloatField()),
                ('mean_motion_ddot', models.FloatField()),
                ('satellite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='tracking.satellite')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

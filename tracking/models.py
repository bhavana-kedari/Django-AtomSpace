from django.db import models

# Create your models here.
class LaunchCountry(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class History(models.Model):
    epoch = models.DateTimeField()
    mean_motion = models.FloatField()
    eccentricity = models.FloatField()
    inclination = models.FloatField()
    ra_of_asc_node = models.FloatField()
    arg_of_pericenter = models.FloatField()
    mean_anomaly = models.FloatField()
    ephemeris_type = models.IntegerField()
    classification_type = models.CharField(max_length=1)
    norad_cat_id = models.IntegerField(unique=True)
    element_set_no = models.IntegerField()
    rev_at_epoch = models.IntegerField()
    bstar = models.FloatField()
    mean_motion_dot = models.FloatField()
    mean_motion_ddot = models.FloatField()

    class Meta:
        abstract = True

class Satellite(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class SatelliteHistory(History):
    satellite = models.ForeignKey(Satellite, on_delete=models.CASCADE, related_name='history')

    def __str__(self):
        return f"History for {self.satellite.name}"

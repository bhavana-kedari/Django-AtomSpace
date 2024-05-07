from django.db import models

# Create your models here.
class LaunchCountry(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Satellite(models.Model):
    name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=20)  # Assuming OBJECT_ID corresponds to NORAD ID
    epoch = models.DateTimeField()
    mean_motion = models.FloatField()
    eccentricity = models.FloatField()
    inclination = models.FloatField()
    ra_of_asc_node = models.FloatField()
    arg_of_pericenter = models.FloatField()
    mean_anomaly = models.FloatField()
    ephemeris_type = models.IntegerField()
    classification_type = models.CharField(max_length=1)
    norad_cat_id = models.IntegerField(unique=True)  # NORAD_CAT_ID
    element_set_no = models.IntegerField()
    rev_at_epoch = models.IntegerField()
    bstar = models.FloatField()
    mean_motion_dot = models.FloatField()
    mean_motion_ddot = models.FloatField()
    launch_country = models.ForeignKey(LaunchCountry, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


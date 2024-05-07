import random
from datetime import datetime
from .models import Satellite, LaunchCountry
import requests

def populate_satellites():
    # Fetch data from the URL
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"
    response = requests.get(url)
    data = response.json()

    # Get all LaunchCountry instances
    launch_countries = LaunchCountry.objects.all()

    # Extract information for each satellite and create instances
    for satellite_data in data:
        # Choose a random LaunchCountry
        random_launch_country = random.choice(launch_countries)

        satellite = Satellite(
            name=satellite_data["OBJECT_NAME"],
            object_id=satellite_data["OBJECT_ID"],
            epoch=datetime.strptime(satellite_data["EPOCH"], "%Y-%m-%dT%H:%M:%S.%f"),
            mean_motion=satellite_data["MEAN_MOTION"],
            eccentricity=satellite_data["ECCENTRICITY"],
            inclination=satellite_data["INCLINATION"],
            ra_of_asc_node=satellite_data["RA_OF_ASC_NODE"],
            arg_of_pericenter=satellite_data["ARG_OF_PERICENTER"],
            mean_anomaly=satellite_data["MEAN_ANOMALY"],
            ephemeris_type=satellite_data["EPHEMERIS_TYPE"],
            classification_type=satellite_data["CLASSIFICATION_TYPE"],
            norad_cat_id=satellite_data["NORAD_CAT_ID"],
            element_set_no=satellite_data["ELEMENT_SET_NO"],
            rev_at_epoch=satellite_data["REV_AT_EPOCH"],
            bstar=satellite_data["BSTAR"],
            mean_motion_dot=satellite_data["MEAN_MOTION_DOT"],
            mean_motion_ddot=satellite_data["MEAN_MOTION_DDOT"],
            launch_country=random_launch_country
        )
        satellite.save()

    print("Satellites populated successfully.")

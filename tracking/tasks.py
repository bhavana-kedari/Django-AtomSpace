from celery import shared_task
from .models import Satellite, SatelliteHistory
from datetime import datetime
import requests

@shared_task
def update_satellites_task():
    # Fetch data from the provided URL
    url = 'https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json'
    response = requests.get(url)
    data = response.json()

    # Extract 10 unique satellite names
    unique_satellite_names = set()
    for satellite_data in data:
        unique_satellite_names.add(satellite_data['OBJECT_NAME'])
        if len(unique_satellite_names) == 10:
            break

    # Iterate over unique satellite names
    for satellite_name in unique_satellite_names:
        satellite, created = Satellite.objects.get_or_create(name=satellite_name)

        # Filter satellite data for the current satellite
        satellite_data = [sat_data for sat_data in data if sat_data['OBJECT_NAME'] == satellite_name]

        # Take the latest 100 epochs for the satellite
        epochs_data = satellite_data[:100]

        # Get existing history for the satellite
        existing_history = SatelliteHistory.objects.filter(satellite=satellite)

        # Extract existing epochs
        existing_epochs = {history.epoch for history in existing_history}

        # Append new epochs to existing history
        new_epochs = []
        for epoch_data in epochs_data:
            epoch = datetime.strptime(epoch_data['EPOCH'], '%Y-%m-%dT%H:%M:%S.%f')
            if epoch not in existing_epochs:
                mean_motion = float(epoch_data['MEAN_MOTION'])
                eccentricity = float(epoch_data['ECCENTRICITY'])
                inclination = float(epoch_data['INCLINATION'])
                ra_of_asc_node = float(epoch_data['RA_OF_ASC_NODE'])
                arg_of_pericenter = float(epoch_data['ARG_OF_PERICENTER'])
                mean_anomaly = float(epoch_data['MEAN_ANOMALY'])
                ephemeris_type = int(epoch_data['EPHEMERIS_TYPE'])
                classification_type = epoch_data['CLASSIFICATION_TYPE']
                norad_cat_id = int(epoch_data['NORAD_CAT_ID'])
                element_set_no = int(epoch_data['ELEMENT_SET_NO'])
                rev_at_epoch = int(epoch_data['REV_AT_EPOCH'])
                bstar = float(epoch_data['BSTAR'])
                mean_motion_dot = float(epoch_data['MEAN_MOTION_DOT'])
                mean_motion_ddot = float(epoch_data['MEAN_MOTION_DDOT'])

                new_epochs.append(SatelliteHistory(
                    satellite=satellite,
                    epoch=epoch,
                    mean_motion=mean_motion,
                    eccentricity=eccentricity,
                    inclination=inclination,
                    ra_of_asc_node=ra_of_asc_node,
                    arg_of_pericenter=arg_of_pericenter,
                    mean_anomaly=mean_anomaly,
                    ephemeris_type=ephemeris_type,
                    classification_type=classification_type,
                    norad_cat_id=norad_cat_id,
                    element_set_no=element_set_no,
                    rev_at_epoch=rev_at_epoch,
                    bstar=bstar,
                    mean_motion_dot=mean_motion_dot,
                    mean_motion_ddot=mean_motion_ddot
                ))

        # Bulk create new epochs
        SatelliteHistory.objects.bulk_create(new_epochs)

        print(f"Updated satellite history for {satellite_name}")

    print("Satellites updated successfully!")

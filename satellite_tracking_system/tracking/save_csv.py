import csv
from .models import Satellite, LaunchCountry

def save_satellites_to_csv():
    satellites = Satellite.objects.all()
    field_names = ['name', 'object_id', 'epoch', 'mean_motion', 'eccentricity', 'inclination', 
                   'ra_of_asc_node', 'arg_of_pericenter', 'mean_anomaly', 'ephemeris_type', 
                   'classification_type', 'norad_cat_id', 'element_set_no', 'rev_at_epoch', 
                   'bstar', 'mean_motion_dot', 'mean_motion_ddot', 'launch_country']

    with open('satellites.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for satellite in satellites:
            writer.writerow({
                'name': satellite.name,
                'object_id': satellite.object_id,
                'epoch': satellite.epoch,
                'mean_motion': satellite.mean_motion,
                'eccentricity': satellite.eccentricity,
                'inclination': satellite.inclination,
                'ra_of_asc_node': satellite.ra_of_asc_node,
                'arg_of_pericenter': satellite.arg_of_pericenter,
                'mean_anomaly': satellite.mean_anomaly,
                'ephemeris_type': satellite.ephemeris_type,
                'classification_type': satellite.classification_type,
                'norad_cat_id': satellite.norad_cat_id,
                'element_set_no': satellite.element_set_no,
                'rev_at_epoch': satellite.rev_at_epoch,
                'bstar': satellite.bstar,
                'mean_motion_dot': satellite.mean_motion_dot,
                'mean_motion_ddot': satellite.mean_motion_ddot,
                'launch_country': satellite.launch_country.name if satellite.launch_country else ''
            })

def save_launch_countries_to_csv():
    launch_countries = LaunchCountry.objects.all()
    field_names = ['name', 'code']

    with open('launch_countries.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for country in launch_countries:
            writer.writerow({
                'name': country.name,
                'code': country.code
            })

# Call the functions to save data to CSV files
save_satellites_to_csv()
save_launch_countries_to_csv()

# utils.py

from tracking.models import Satellite

def cleanup_satellites():
    # Query all satellite entries
    all_satellites = Satellite.objects.all()

    # Limit to 600 entries
    selected_satellites = all_satellites[:600]

    # Get IDs of excess entries
    excess_ids = all_satellites[600:].values_list('id', flat=True)

    # Delete excess entries from the database
    Satellite.objects.filter(id__in=excess_ids).delete()

cleanup_satellites()
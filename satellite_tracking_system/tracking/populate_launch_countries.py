import random
from .models import Satellite, LaunchCountry
from faker import Faker

import random
from .models import LaunchCountry
from faker import Faker

def populate_launch_countries():
    fake = Faker()

    # Delete existing LaunchCountry instances
    LaunchCountry.objects.all().delete()

    for _ in range(400):
        # Generate a random country name and code using Faker
        country_name = fake.country()
        country_code = fake.country_code()

        # Create LaunchCountry instance
        LaunchCountry.objects.create(name=country_name, code=country_code)

    print("Countries populated successfully.")

# Call the function to populate launch countries
populate_launch_countries()


# def delete_all_launch_countries():
#     LaunchCountry.objects.all().delete()
#     print("All LaunchCountries deleted successfully.")

# # Call the function to delete all launch countries
# delete_all_launch_countries()



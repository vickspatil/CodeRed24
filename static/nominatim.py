from geopy.geocoders import Nominatim
from exif import latitude
from exif import longitude 


def get_location_text(latitude, longitude):
    # Create a geocoder instance with Nominatim
    geolocator = Nominatim(user_agent="location_finder")

    # Combine latitude and longitude into a tuple
    location = (latitude, longitude)

    try:
        # Use reverse geocoding to get the address
        location_info = geolocator.reverse(location, language='en')

        # Extract and return the formatted address
        return location_info.address

    except Exception as e:
        print(f"Error: {e}")
        return None

location_text = get_location_text(latitude, longitude)

if location_text:
    print(f"Location Text: {location_text}")
else:
    print("Failed to retrieve location text.")

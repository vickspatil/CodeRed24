import exifread

def extract_location(image_path):
    try:
        # Open the image
        with open(image_path, 'rb') as file:
            # Read EXIF data
            tags = exifread.process_file(file)

            # Extract GPS info
            lat_ref = tags.get('GPS GPSLatitudeRef', None)
            lon_ref = tags.get('GPS GPSLongitudeRef', None)
            lat = tags.get('GPS GPSLatitude', None)
            lon = tags.get('GPS GPSLongitude', None)

            if lat_ref and lon_ref and lat and lon:
                lat_val = lat.values[0] + lat.values[1]/60 + lat.values[2]/lat.values[3]
                lon_val = lon.values[0] + lon.values[1]/60 + lon.values[2]/lon.values[3]

                # Adjust latitude and longitude based on reference
                latitude = lat_val if lat_ref.values == 'N' else -lat_val
                longitude = lon_val if lon_ref.values == 'E' else -lon_val

                return {
                    "latitude": latitude,
                    "longitude": longitude
                }

    except Exception as e:
        return {"error": str(e)}

    return {"error": "No location information found."}

# Example usage
image_path = "D:\CodeRed\img_1.jpg"
location_info = extract_location(image_path)

if "error" in location_info:
    print(f"Error: {location_info['error']}")
else:
    print(f"Latitude: {location_info['latitude']}, Longitude: {location_info['longitude']}")
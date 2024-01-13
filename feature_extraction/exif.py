from PIL import Image
from datetime import datetime
import piexif

def extract_metadata(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Extract EXIF data
        exif_data = img._getexif()

        # Check if there is EXIF data
        if exif_data is not None:
            # Extract GPS info
            gps_info = exif_data.get(34853, None)

            if gps_info:
                lat = gps_info[2][0] + gps_info[2][1]/60 + gps_info[2][2]/3600
                lon = gps_info[4][0] + gps_info[4][1]/60 + gps_info[4][2]/3600

                # Extract date and time
                date_time_str = exif_data.get(36867, None)
                if date_time_str:
                    date_time = datetime.strptime(date_time_str, "%Y:%m:%d %H:%M:%S")

                    return {
                        "latitude": lat,
                        "longitude": lon,
                        "datetime": date_time
                    }

    except Exception as e:
        return {"error": str(e)}

    return {"error": "No metadata found."}
image_path="D:\CodeRed\img_4.jpg"
metadata=extract_metadata(image_path)
lat=float(metadata['latitude'])
longi=float(metadata['longitude'])
if "error" in metadata:
    print(f"Error: {metadata['error']}")
else:
    print(f"Latitude : {lat}, Longitude : {longi}")
    print(f"Date & Time: {metadata['datetime']}")
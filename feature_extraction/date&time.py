from PIL import Image
import piexif
from datetime import datetime

def extract_date_time(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Extract EXIF data
        exif_data = img._getexif()

        # Check if there is EXIF data
        if exif_data is not None:
            # Extract date and time
            date_time_str = exif_data.get(36867, None)

            if date_time_str:
                date_time = datetime.strptime(date_time_str, "%Y:%m:%d %H:%M:%S")

                return {"datetime": date_time}

    except Exception as e:
        return {"error": str(e)}

    return {"error": "No date and time information found."}

# Example usage
image_path = "D:\CodeRed\img_1.jpg"
date_time_info = extract_date_time(image_path)

if "error" in date_time_info:
    print(f"Error: {date_time_info['error']}")
else:
    print(f"Date and Time: {date_time_info['datetime']}")

from flask import Flask, render_template, request
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'D:/CodeRed/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        elif event.src_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            process_uploaded_file(event.src_path)

def process_uploaded_file(file_path):
    # Extract metadata when a new image is added
    metadata = extract_metadata(file_path)

    if "error" in metadata:
        print(f"Error: {metadata['error']}")
    else:
        latitude = float(metadata['latitude'])
        longitude = float(metadata['longitude'])
        print(f"Latitude: {latitude}, Longitude: {longitude}")
        print(f"Date & Time: {metadata['datetime']}")

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

def start_file_watcher():
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=UPLOAD_FOLDER, recursive=False)
    observer.start()

if __name__ == '__main__':
    start_file_watcher()
    app.run(debug=True)

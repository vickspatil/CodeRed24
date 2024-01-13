import subprocess
from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import piexif

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the uploaded image to a temporary file
        temp_path = "temp_image.jpg"
        file.save(temp_path)

        # Read the uploaded image
        image = cv2.imread(temp_path)

        # Run program with Exif data check
        run_program_with_exif(temp_path)

        # Remove the temporary file
        os.remove(temp_path)

        return "Image uploaded successfully"

def run_program_with_exif(temp_path):
    try:
        exif_data = piexif.load(temp_path)
        if exif_data:
            print("Exif data found. Running exif.py...")
            subprocess.run(['python', 'codes\exif.py'])
        else:
            print("No Exif data found. Running app.py...")
            subprocess.run(['python', 'codes\app.py'])
    except (IOError, ValueError, piexif.InvalidImageDataError):
        print("Error opening the image or retrieving Exif data.")

if __name__ == "__main__":
    app.run(debug=True, port=5001)

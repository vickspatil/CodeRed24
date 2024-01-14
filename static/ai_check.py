import exifread

def check_ai_generated(image_path):
    # Read EXIF data from the image
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)

    # Check for specific EXIF tags or other features
    confidence_score = tags.get('Xmp.dc.confidence', None)
    c2pa_sign = tags.get('C2PA.Signature', None)

    # Add more conditions based on your knowledge of the specific features
    if confidence_score and float(confidence_score) > 0.8:
        return "AI-generated"
    elif c2pa_sign:
        return "C2PA-signed"
    else:
        return "Real image"

# Example usage
image_path = 'path/to/your/image.jpg'
result = check_ai_generated(image_path)
print(f"The image is identified as: {result}")

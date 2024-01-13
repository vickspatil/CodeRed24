from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)

# Load the Keras model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = [line.strip() for line in open("labels.txt", "r")]

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

        # Resize the image to (224, 224)
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Make the image a numpy array and reshape it to the model's input shape
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predict using the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Display the result
        result = f"Class: {class_name[2:]}, Confidence Score: {str(np.round(confidence_score * 100))[:-2]}%"

        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

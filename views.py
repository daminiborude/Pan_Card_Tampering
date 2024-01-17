# Important imports 
from app import app
from flask import request, render_template
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
 
# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTNG_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'

# Route to home page
# ... (imports and configurations remain the same)

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():
    # Execute if request is get
    if request.method == "GET":
        return render_template("index.html")

    # Execute if request is post
    if request.method == "POST":
        # Get uploaded image
        file_upload = request.files['file_upload']

        # Resize and save the uploaded image
        with Image.open(file_upload).resize((250, 160)) as uploaded_image:
            uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        # Resize and save the original image to ensure both uploaded and original match in size
        with Image.open(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg')).resize((250, 160)) as original_image:
            original_image.save(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg'))

        # Read uploaded and original image as arrays
        original_image = cv2.imread(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg'))
        uploaded_image = cv2.imread(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        # ... (rest of the code remains the same)

    return render_template('index.html', pred=str(round(score * 100, 2)) + '%' + ' correct')

# Main function
if __name__ == '__main__':
    app.run(debug=True)

import os
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_and_insert_logo():
    if request.method == 'POST':
        logo = request.files['logo']
        logo_img = Image.open(logo)
        logo_size = (150, 150)
        logo_img = logo_img.resize(logo_size)

        uploaded_images = request.files.getlist('images[]')
        output_folder = request.form.get('output_folder')

        for img in uploaded_images:
            main_image = Image.open(img)
            position = (main_image.width - logo_img.width, 10)
            main_image.paste(logo_img, position, logo_img)
            output_path = f'{output_folder}/{img.filename}'
            main_image.save(output_path)

        return render_template('output.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
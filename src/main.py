from flask import Flask
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def insertWaterMark(filename):
    if not allowed_file(filename):
        print("File not allowed")
        return {'status': 'failed', 'message': 'Improper filename'}, 400

    #try:
    # Open the meme image
    img = Image.open(filename).convert("RGBA")
    # Open the watermark image
    watermark = Image.open('download.jpeg').convert("RGBA")
    # Add the watermark to the image
    img.paste(watermark, (0, 0), watermark)
    # Save the image
    newFilename = 'memes/ZZ' + filename
    # Convert to RGB to avoid problems with non-PNG files
    img = img.convert("RGB")
    img.save(newFilename)

    print("New filename: ", newFilename)
    return {'status': 'success', 'image': f'static/petpets/{newFilename}'}, 200

    # except:
    #     print("Error")
    #     return {'status': 'failed', 'message': 'Something went wrong'}, 500


@app.route('/')
def hello():
    insertWaterMark('download.jpeg')
    return "Hello World!"



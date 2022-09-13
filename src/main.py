from flask import Flask
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
import os

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
    watermark = Image.open('assets/watermark.jpeg').convert("RGBA")
    # Add the watermark to the image
    img.paste(watermark, (0, 0), watermark)
    # Save the image
    newFilename = filename.rsplit('/', 1)[1]
    newFilename = 'memes/ZZ' + newFilename
    # Convert to RGB to avoid problems with non-PNG files
    img = img.convert("RGB")
    img.save(newFilename)

    print("New filename: ", newFilename)
    return {'status': 'success', 'image': f'memes/{newFilename}'}, 200

    # except:
    #     print("Error")
    #     return {'status': 'failed', 'message': 'Something went wrong'}, 500


def getMemes():
    memes = []
    for filename in os.listdir('memes'):
        if allowed_file(filename):
            memes.append(filename)
    return memes


def editHTML(memes : list):
    # Load file and parse with BeautifulSoup
    html = open("src/index.html")
    print("HTML loaded")
    soup = BeautifulSoup(html, "html.parser")
    print("HTML parsed")
    for meme in memes:
        # Create a new div
        newDiv = soup.new_tag("div")
        # Create a new img tag
        newImg = soup.new_tag("img")
        # Set the src of the img tag
        newImg['src'] = f'memes/{meme}'
        # Add the img tag to the div
        newDiv.append(newImg)
        # Add the div to the memes div
        soup.find(id="memes").append(newDiv)
        
    # Write the new HTML to new file
    with open("output.html", "w") as file:
        file.write(str(soup))
    

@app.route('/')
def main():
    insertWaterMark('uploads/download.jpeg')
    memes = getMemes()
    editHTML(memes)
    return "h"



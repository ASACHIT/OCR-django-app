from django.shortcuts import render
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" # Path to tesseract.exe
import numpy as np
from PIL import Image
# Create your views here.

def homepage(request):
    if request.method == 'POST':
        # get image from "image" form field
        img = request.FILES['imagefile']
        # convert image to numpy array
        img = np.array(Image.open(img))
        # extract text from image
        text = pytesseract.image_to_string(img)
        # return text
        return render(request, 'home.html', context={'ocr': text})
    return render(request, "home.html")
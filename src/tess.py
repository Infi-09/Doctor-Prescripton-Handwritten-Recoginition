import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def tesse(path):
    image_path_in_colab=path
    extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab))
    return extractedInformation
    # print(extractedInformation)

# tesse('demo/test_lab.jpg')
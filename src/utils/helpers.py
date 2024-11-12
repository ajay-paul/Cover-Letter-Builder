from PIL import Image
from io import BytesIO
import pytesseract
import os

def save_image(image_data, file_path):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    full_path = os.path.join(root_dir, file_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "wb") as f:
        f.write(image_data)
    print("Data saved! \n ")

def extract_text_from_image(image_data):
    image = Image.open(BytesIO(image_data))
    text = pytesseract.image_to_string(image)
    print("Text extracted! \n ")
    return text

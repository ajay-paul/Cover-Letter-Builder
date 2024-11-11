from PIL import Image
from io import BytesIO
import pytesseract
import os

# Function to save image data to a specified file path

def save_image(image_data, file_path):
    # Get the absolute path from the project root directory
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    full_path = os.path.join(root_dir, file_path)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # Save the image to the file path
    with open(full_path, "wb") as f:
        f.write(image_data)
    print(f"Image saved to {full_path}")

# Function to extract text from an image using pytesseract
def extract_text_from_image(image_data):
    image = Image.open(BytesIO(image_data))
    text = pytesseract.image_to_string(image)
    print("Extracted Text from Screenshot:")
    print(text)
    return text

import cv2
import numpy as np

def load_and_preprocess(image_path: str):
    image = cv2.imread(str(image_path))
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    
    # Resize to standardize processing
    image = cv2.resize(image, (512, 512))
    
    # Convert to grayscale for simple differencing
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    return image, gray_image

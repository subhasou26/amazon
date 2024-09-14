import os
from PIL import Image
import numpy as np

# Function to preprocess images
def preprocess_image(image_path, output_size=(224, 224), grayscale=True):
    # Open the image
    img = Image.open(image_path)
    
    # Convert to grayscale if specified
    if grayscale:
        img = img.convert('L')  # 'L' mode is for grayscale

    # Resize the image
    img = img.resize(output_size)
    
    # Convert to NumPy array
    img_array = np.array(img, dtype=np.float32)
    
    # Normalize pixel values to [0, 1]
    img_array /= 255.0
    
    return img_array

# Function to preprocess all images in a folder
def preprocess_images_in_folder(input_folder, output_folder, output_size=(224, 224), grayscale=True):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(input_folder, filename)
            
            # Preprocess the image
            preprocessed_image = preprocess_image(image_path, output_size, grayscale)
            
            # Convert the NumPy array back to an image and save it
            preprocessed_img = Image.fromarray((preprocessed_image * 255).astype(np.uint8))
            output_path = os.path.join(output_folder, filename)
            preprocessed_img.save(output_path)
            
            print(f"Processed and saved: {output_path}")

# Example usage
input_folder = './images'
output_folder = './images_out'

preprocess_images_in_folder(input_folder, output_folder, output_size=(224, 224), grayscale=True)
import os
from rembg import remove
from PIL import Image

# Define the input and output folder paths
input_folder = './input'
output_folder = './output'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Construct the input and output file paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Load the input image
        input_image = Image.open(input_path)

        # Remove the background from the image
        output_image = remove(input_image)

        # Convert RGBA image to RGB
        if output_image.mode == 'RGBA':
            output_image = output_image.convert('RGB')

        # Save the output image
        output_image.save(output_path)

        print(f"Processed image: {filename}")

print("All images processed successfully.")

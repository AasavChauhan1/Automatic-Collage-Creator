from PIL import Image
import os

def create_collage_for_subfolders(parent_folder, output_name_prefix="_collage", grid_size=(3, 3), image_size=(299, 299)):
    """
    Create a collage for each subfolder in the given parent folder and name it to appear first in the folder.

    Parameters:
        parent_folder (str): Path to the main folder containing subfolders.
        output_name_prefix (str): Prefix for the output collage image to ensure it appears first in the folder.
        grid_size (tuple): Number of rows and columns in the collage (default is 3x3).
        image_size (tuple): Size of each image in the collage (default is 300x300 pixels).
    """
    print(f"Scanning parent folder: {parent_folder}")

    # Iterate through each subfolder in the parent folder
    for subfolder in os.listdir(parent_folder):
        subfolder_path = os.path.join(parent_folder, subfolder)

        # Skip if it's not a directory
        if not os.path.isdir(subfolder_path):
            print(f"Skipping {subfolder}: Not a directory.")
            continue

        print(f"Processing subfolder: {subfolder}")

        # Get all image files in the subfolder
        image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
        print(f"Found {len(image_files)} images in {subfolder}.")

        # Ensure there are enough images to create a grid
        if len(image_files) < grid_size[0] * grid_size[1]:
            print(f"Skipping {subfolder}: Not enough images for a {grid_size[0]}x{grid_size[1]} collage.")
            continue

        # Create a blank canvas for the collage
        collage_width = grid_size[1] * image_size[0]
        collage_height = grid_size[0] * image_size[1]
        collage = Image.new('RGB', (collage_width, collage_height), color=(255, 255, 255))

        # Place each image into the collage
        for index, img_file in enumerate(image_files[:grid_size[0] * grid_size[1]]):
            img_path = os.path.join(subfolder_path, img_file)
            print(f"Adding image to collage: {img_path}")
            img = Image.open(img_path).resize(image_size)
            x_offset = (index % grid_size[1]) * image_size[0]
            y_offset = (index // grid_size[1]) * image_size[1]
            collage.paste(img, (x_offset, y_offset))

        # Save the collage in the same subfolder with a prefixed name
        output_name = f"{output_name_prefix}.jpg"
        output_path = os.path.join(subfolder_path, output_name)
        collage.save(output_path)
        print(f"Collage created and saved as {output_name} in {subfolder}")

# Example usage
parent_folder_path = r"D:\TELEGRAM\Profile Paradise\Downloaded\collage"  # Replace with your folder path
create_collage_for_subfolders(parent_folder_path)

import dlib
from PIL import Image, ImageDraw
import numpy as np
import os

# Folder with original images
folder_path = r"C:\codesheft tasks\Face_Recognition_Project\known _faces"

# Folder to save images with rectangles
output_folder = r"C:\codesheft tasks\Face_Recognition_Project\output_faces"
os.makedirs(output_folder, exist_ok=True)

# Initialize dlib face detector
detector = dlib.get_frontal_face_detector()

# Loop through all images in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_path = os.path.join(folder_path, filename)
        
        # Load image
        img = np.array(Image.open(image_path))
        
        # Detect faces
        faces = detector(img, 1)
        print(f"{filename}: {len(faces)} face(s) detected")
        
        # Draw rectangles on the image
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        for face in faces:
            draw.rectangle([face.left(), face.top(), face.right(), face.bottom()], outline="red", width=3)
        
        # Save annotated image
        output_path = os.path.join(output_folder, filename)
        img_pil.save(output_path)
        print(f"Saved annotated image: {output_path}")

import face_recognition
import os
import pickle

known_encodings = []
known_names = []

# Loop through each person’s folder
known_faces_dir = r"C:\codesheft tasks\Face_Recognition_Project\known_faces"
for person_name in os.listdir(known_faces_dir):
    person_folder = os.path.join(known_faces_dir, person_name)
    if not os.path.isdir(person_folder):
        continue
    for image_file in os.listdir(person_folder):
        if image_file.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(person_folder, image_file)
            img = face_recognition.load_image_file(img_path)
            encodings = face_recognition.face_encodings(img)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(person_name)

# Save encodings to a file
with open("known_face_encodings.pkl", "wb") as f:
    pickle.dump((known_encodings, known_names), f)

print("Encodings saved for", len(known_names), "faces.")

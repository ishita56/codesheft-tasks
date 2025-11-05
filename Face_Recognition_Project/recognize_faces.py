import face_recognition
import cv2
import pickle
import os

# Load encodings
with open("known_face_encodings.pkl", "rb") as f:
    data = pickle.load(f)

# Check if data is a tuple or dict
if isinstance(data, tuple):
    encodings_list = data[0]
    names_list = data[1]
elif isinstance(data, dict):
    encodings_list = data["encodings"]
    names_list = data["names"]
else:
    raise ValueError("Encodings file has unsupported format.")

# Open webcam
video_capture = cv2.VideoCapture(0)
print("Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces and get encodings
    boxes = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, boxes)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(encodings_list, encoding)
        name = "Unknown"

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIdxs:
                counts[names_list[i]] = counts.get(names_list[i], 0) + 1
            name = max(counts, key=counts.get)

        names.append(name)

    # Draw boxes and labels
    for ((top, right, bottom, left), name) in zip(boxes, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()

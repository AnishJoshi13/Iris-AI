import os
import cv2
import face_recognition
from src.Robo_Functions.Face_data_Collection import capture_image

known_faces_dir = "C:\\IrisAI_dir\\src\\Robo_Functions\\faces"

def recognize_faces():
    # Load the known faces and their names
    known_faces = {}
    for filename in os.listdir(known_faces_dir):
        name = os.path.splitext(filename)[0]
        image_path = os.path.join(known_faces_dir, filename)
        face_image = face_recognition.load_image_file(image_path)
        known_faces[name] = face_image

    # Encode the known faces
    known_encodings = {}
    for name, face_image in known_faces.items():
        face_encoding = face_recognition.face_encodings(face_image)[0]
        known_encodings[name] = face_encoding

    # Initialize the video capture
    video_capture = cv2.VideoCapture(0)

    capture_image_flag = False  # Flag to indicate if capture image is required

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Detect faces in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Iterate through each detected face
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare the detected face with the known faces
            matches = face_recognition.compare_faces(list(known_encodings.values()), face_encoding)
            name = "Unknown"

            # Check if there is a match
            if True in matches:
                matched_index = matches.index(True)
                name = list(known_encodings.keys())[matched_index]

            # Draw the rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Display the name outside the rectangle
            label_background_color = (0, 0, 255)
            label_text_color = (255, 255, 255)
            label_position = (left, bottom + 20)  # Adjust position as needed
            cv2.rectangle(frame, (left, bottom), (right, bottom + 30), label_background_color, cv2.FILLED)
            cv2.putText(frame, name, label_position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, label_text_color, 2)

            if name == "Unknown":
                # Ask if the person is unknown
                cv2.putText(frame, "Do you want me to remember you? (Y/N)", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # Wait for user input
                key = cv2.waitKey(1) & 0xFF
                if key == ord('y') or key == ord('Y'):
                    capture_image_flag = True
                elif key == ord('n') or key == ord('N'):
                    capture_image_flag = False
                    break

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Capture image if required
        if capture_image_flag:
            capture_image()
            capture_image_flag = False
            # Recall the whole function
            video_capture.release()
            cv2.destroyAllWindows()
            recognize_faces()

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture
    video_capture.release()
    cv2.destroyAllWindows()

# # Call the function to start recognizing faces
# recognize_faces()

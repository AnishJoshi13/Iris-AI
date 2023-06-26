import cv2
import face_recognition
import time

def capture_image():
    # Open the default camera (index 0)
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        raise ValueError("Unable to open video source")

    start_time = time.time()
    while True:
        # Read a frame from the video source
        ret, frame = video_capture.read()

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)

        if len(face_locations) > 0:
            # Display the captured image
            cv2.imshow("Captured Image", frame)

            # Prompt the user to enter a name for the image
            image_name = input("Enter the name for the image: ")

            # Define the directory to save the image
            save_directory = "C:\\IrisAI_dir\\src\\Robo_Functions\\faces\\"

            # Save the captured image with the provided name
            image_path = save_directory + image_name + ".jpg"
            cv2.imwrite(image_path, frame)

            print(f"Image saved successfully as: {image_path}")
            break

        current_time = time.time()
        # Break the loop if no face is detected for 1 minute
        if current_time - start_time >= 60:
            print("No face detected. Exiting...")
            break

        # Display "No face detected" message if no face is found
        cv2.putText(frame, "No face detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Capturing Image...", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the video capture
    video_capture.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


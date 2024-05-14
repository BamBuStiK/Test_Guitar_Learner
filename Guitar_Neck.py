import cv2

def process_video(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error: Unable to open video file")
        return

    # Read frames from the video
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If the frame was not read successfully, break the loop
        if not ret:
            break

        # Display the frame
        cv2.imshow('Frame', frame)

        # Check for key input
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def main():
    video_path = "Saved_Vids/Test_Sample.f136.mp4"  # Path to the downloaded video
    process_video(video_path)

if __name__ == "__main__":
    main()

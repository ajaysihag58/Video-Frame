import cv2
import os


def extract_frames(video_path, output_folder):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    # Check if the video opened successfully
    if not video_capture.isOpened():
        print("Error: Unable to open video file.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0
    while True:
        # Read a single frame from the video
        ret, frame = video_capture.read()
        # If no frame is read, break the loop
        if not ret:
            break
        # Save the frame as an image
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        # Increment frame count
        frame_count += 1

    # Release the video capture object
    video_capture.release()
    print(f"{frame_count} frames extracted and saved to {output_folder}")


# Example usage
if __name__ == "__main__":
    # Replace 'Video_source_path' with your actual video source path below
    video_path = r"Video_source_path"
    # Replace 'Frame_output_path' with your actual path for Storing Output Frames below
    output_folder = r"Frame_output_path"
    extract_frames(video_path, output_folder)

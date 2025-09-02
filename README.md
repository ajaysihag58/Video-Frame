# Video to Frame Extractor

This project provides a simple Python script to extract frames from a video file and save them as images using OpenCV.

## Requirements
- Python 3.x
- OpenCV (`cv2`)

## Installation
Install OpenCV if you haven't already:
```bash
pip install opencv-python
```

## Usage
1. Edit the `import cv2.py` file to set your `video_path` and `output_folder`.
2. Run the script:
```bash
python "import cv2.py"
```
3. The frames will be saved as JPG images in the specified output folder.

## Example
```
video_path = r"C:\Users\ajsih\OneDrive\Pictures\Camera Roll\111.mp4"
output_folder = r"C:\Users\ajsih\OneDrive\Pictures\Camera Roll\extracted_frames"
extract_frames(video_path, output_folder)
```

## Function
### extract_frames(video_path, output_folder)
Extracts all frames from the video at `video_path` and saves them as JPG images in `output_folder`.

---
**Note:** The script will create the output folder if it does not exist.

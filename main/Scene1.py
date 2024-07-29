import os
import cv2
import numpy as np
from PIL import Image
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

def overlay_image_on_frames(frame_folder, image_path, output_video_path, frame_rate=30):
    # Load the overlay image as RGB
    try:
        overlay_image_pil = Image.open(image_path).convert("RGB")
        overlay_image_np = np.array(overlay_image_pil)
    except Exception as e:
        print(f"Error loading overlay image: {e}")
        return
    
    if overlay_image_np is None:
        raise ValueError(f"Error loading image from path: {image_path}")

    # Convert RGB overlay image to BGR
    overlay_image_np = cv2.cvtColor(overlay_image_np, cv2.COLOR_RGB2BGR)

    # Read all frames from the folder
    frame_files = sorted([os.path.join(frame_folder, f) for f in os.listdir(frame_folder) if f.endswith(".png")])
    
    if not frame_files:
        print("No frames found in the directory.")
        return
    
    # Use the first frame to get dimensions
    first_frame = cv2.imread(frame_files[0], cv2.IMREAD_COLOR)
    if first_frame is None:
        print(f"Error reading the first frame: {frame_files[0]}")
        return

    height, width = first_frame.shape[:2]
    
    # Resize the overlay image to match the frame dimensions
    overlay_image_pil = Image.fromarray(cv2.cvtColor(overlay_image_np, cv2.COLOR_BGR2RGB)).resize((width, height), Image.LANCZOS)
    overlay_image_np = np.array(overlay_image_pil)
    
    # Convert resized overlay image to BGR
    overlay_image_np = cv2.cvtColor(overlay_image_np, cv2.COLOR_RGB2BGR)
    
    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))
    
    for frame_file in frame_files:
        frame = cv2.imread(frame_file, cv2.IMREAD_COLOR)
        
        if frame is None:
            print(f"Error reading frame: {frame_file}")
            continue
        
        # Combine the overlay image with the frame
        combined_frame_np = cv2.addWeighted(frame, 1.0, overlay_image_np, 1.0, 0)  # Adjust alpha if needed
        
        # Write the frame to the video
        video_writer.write(combined_frame_np)
    
    video_writer.release()
    print(f"Video saved as {output_video_path}")


# Example usage
frame_folder = "Video Frame/Aft"  # Folder containing the extracted frames
image_path = "Pic/Scene1/2.png"  # Path to the overlay image
output_video_path = "Processed Pic/Scene1.mp4"  # Path to save the final video

overlay_image_on_frames(frame_folder, image_path, output_video_path, frame_rate=30)

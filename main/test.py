from moviepy.editor import VideoFileClip

def check_frame_rate(video_path):
    clip = VideoFileClip(video_path)
    return clip.fps

# Check the frame rate of your input and output videos
input_frame_rate = check_frame_rate("Pic/Scene1/Sakura.mp4")
output_frame_rate = check_frame_rate("Processed Pic/Scene1.mp4")

print(f"Input Frame Rate: {input_frame_rate}")
print(f"Output Frame Rate: {output_frame_rate}")

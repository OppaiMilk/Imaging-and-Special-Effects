import os
import cv2
import numpy as np
from PIL import Image
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip

def add_audio_to_video(video_path, audio_path, output_path):
    # Load video and audio files
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    
    # Set the audio of the video clip
    video_clip = video_clip.set_audio(audio_clip)
    
    # Write the result to a file
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

output_video_path = "Pic/Scene/Scene1.mp4"
audio_path = "Pic/Scene1/Wind.mp4"  # Path to the MP3 audio file
final_output_path = "Processed Pic/Scene1.mp4"  # Path to save the final video with audio
add_audio_to_video(output_video_path, audio_path, final_output_path)



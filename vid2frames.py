from pytubefix import YouTube
from moviepy import VideoFileClip
import os


def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"\rHerunterladen: {percentage:.2f}% abgeschlossen", end="")


def download_youtube_video(url, output_path="video.mp4"):
    yt = YouTube(url, on_progress_callback=progress_callback)
    stream = yt.streams.get_highest_resolution()
    stream.download(filename=output_path)
    print(f"\nVideo heruntergeladen: {output_path}")
    return output_path


def video_to_frames(video_path):
    frames_folder = "frames"
    if not os.path.exists(frames_folder):
        os.makedirs(frames_folder)

    try:
        video = VideoFileClip(video_path)
        total_frames = int(video.fps * video.duration)
        for i, frame in enumerate(video.iter_frames(with_times=False)):
            frame_filename = os.path.join(frames_folder, f"frame_{i:04d}.jpg")
            frame.saveframe(frame_filename)
            progress = (i / total_frames) * 100
            print(f"\rUmwandeln: {progress:.2f}% abgeschlossen", end="")
        print(f"\nExtrahiert {i + 1} Frames nach {frames_folder}")
    except Exception as e:
        print(f"Fehler beim Verarbeiten des Videos: {e}")


# Beispielaufruf der Funktionen
video_url = "https://youtu.be/kXWKaylIhCg?si=TUsuSanc_mVlnKU3"
video_path = download_youtube_video(video_url)
video_to_frames(video_path)

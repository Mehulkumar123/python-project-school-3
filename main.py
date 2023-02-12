from pytube import YouTube
from pytube import Playlist
import shutil
import os

# Function to download a video
def download_video(link, user_path):
    try:
        video = YouTube(link)
        video_title = video.title
        mp4_video = video.streams.get_highest_resolution()
        file_path = os.path.join(user_path, f"{video_title}.mp4")
        
        if os.path.exists(file_path):
            print(f"Video '{video_title}' already exists. Skipping...")
        else:
            mp4_video.download(user_path)
            print(f"Video '{video_title}' downloaded successfully.")
    except Exception as e:
        print(f"An error occurred while downloading the video: {e}")

# Function to download a playlist
def download_playlist(link, path):
    try:
        mp4_video = Playlist(link)
        for video in mp4_video.videos:
            file_name = video.title + '.mp4'
            file_path = os.path.join(path, file_name)
            if os.path.exists(file_path):
                print(f"Skipping {file_name}, as it already exists.")
                continue
            vid = video.streams.get_highest_resolution().download()
            shutil.move(vid, path)
            print(f"Downloaded {file_name}.")
    except Exception as e:
        print(f"An error occurred while downloading the playlist: {e}")

# Keep downloading videos or playlists until the user chooses to exit
while True:
    choice = input("Do you want to download a video or a playlist? (video/playlist/exit): ")
    
    if choice.lower() == "exit":
        break
    
    link = input("Enter the link: ")
    path = input("Enter the path to save the video/playlist: ")

    if choice.lower() == "video":
        download_video(link, path)
        print("Video download complete!")
    elif choice.lower() == "playlist":
        download_playlist(link, path)
        print("Playlist download complete!")
    else:
        print("Invalid choice. Please try again.")

from pytube import YouTube
from pytube import Playlist
import shutil
import os

# Function to download a single video
def download_video(link, user_path):
    # Create a YouTube object from the link
    video = YouTube(link)
    
    # Get the title of the video
    video_title = video.title
    
    # Get the highest resolution video stream
    mp4_video = video.streams.get_highest_resolution()
    
    # Create the file path to save the video
    file_path = os.path.join(user_path, f"{video_title}.mp4")
    
    # Check if the file already exists
    if os.path.exists(file_path):
        print(f"Video '{video_title}' already exists. Skipping...")
    else:
        # Download the video
        mp4_video.download(user_path)
        print(f"Video '{video_title}' downloaded successfully.")

# Function to download a playlist
def download_playlist(link, path):
    # Create a Playlist object from the link
    mp4_video = Playlist(link)
    
    # Loop through the videos in the playlist
    for video in mp4_video.videos:
        # Get the title of the video
        file_name = video.title + '.mp4'
        
        # Create the file path to save the video
        file_path = os.path.join(path, file_name)
        
        # Check if the file already exists
        if os.path.exists(file_path):
            print(f"Skipping {file_name}, as it already exists.")
            continue
        
        # Download the video
        vid = video.streams.get_highest_resolution().download()
        
        # Move the downloaded video to the specified folder
        shutil.move(vid, path)
        print(f"Downloaded {file_name}.")

# Keep downloading videos or playlists until the user chooses to exit
while True:
    # Ask the user if they want to download a video or a playlist
    choice = input("Do you want to download a video or a playlist? (video/playlist/exit): ")
    
    # If the user chooses to exit, break the loop
    if choice.lower() == "exit":
        break
    
    # Get the link to the video/playlist
    link = input("Enter the link: ")
    
    # Get the folder to save the video/playlist
    path = input("Enter the path to save the video/playlist: ")

    # If the user chose to download a video, call the `download_video` function
    if choice.lower() == "video":
        download_video(link, path)
        print("Video download complete!")
    # If the user chose to download a playlist, call the `download_playlist` function
    elif choice.lower() == "playlist":
        download_playlist(link, path)
        print("Playlist download complete!")
    # If the user made an invalid choice, ask them to try again
    else:
        print("Invalid choice. Please try again.")

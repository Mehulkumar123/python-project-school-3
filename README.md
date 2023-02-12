# python-project-school-3
This is a Python script that allows a user to download either a single video or a playlist from YouTube. The script uses the Pytube library to download the videos. The user is prompted to choose whether they want to download a video or a playlist, and then enter the link to the video/playlist and the folder where they want to save it.

The download_video function takes the link to the video and the folder path as input and uses the Pytube library to download the video. It first creates a YouTube object from the link and gets the title of the video. Then it gets the highest resolution video stream and creates the file path to save the video. The function checks if the file already exists in the specified folder, and if it does, it skips the download. If the file does not exist, it downloads the video and saves it in the specified folder.

The download_playlist function takes the link to the playlist and the folder path as input and uses the Pytube library to download all the videos in the playlist. It creates a Playlist object from the link and loops through all the videos in the playlist. For each video, it gets the title of the video and creates the file path to save it. The function checks if the file already exists in the specified folder, and if it does, it skips the download. If the file does not exist, it downloads the video and saves it in the specified folder.

The script continues to prompt the user to download either a video or a playlist until they choose to exit.

# python-project-school-3
This code downloads YouTube videos or playlists.
The user is prompted to choose whether they want
to download a video or a playlist, and then enter 
the link to the video or playlist and the path to
save the downloaded videos.
The code uses the pytube library to download videos
and playlists from YouTube. It first creates a 
YouTube object from the link and gets the highest
resolution video stream for the video. Then, it 
saves the video to the specified folder with the 
title of the video as the file name.
For playlists, the code uses the Playlist object
from pytube to get all the videos in the playlist
and downloads them one by one. It skips videos 
that have already been downloaded and moves the
downloaded video to the specified folder.
The code runs in a loop and continues to 
download videos or playlists until the user
chooses to exit.

The library used in this code is pytube - a library for downloading videos from YouTube.

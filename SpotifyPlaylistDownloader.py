# Imports for track details
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

# Imports for parsing URL of the video song
import urllib.request
from urllib.parse import quote
import re

# Imports for track download from youtube
import youtube_dl
import os
import shutil

'''
1. Get track and artist names using spotify API
2. Webcrawler to search for the song on youtube and parse the URL
3. Download mp3 format of the song from the parsed URL
'''

def AuthenticationWithoutUser(cid, secret):
    ccm = SpotifyClientCredentials(client_id = cid, client_secret = secret)
    sp = spotipy.Spotify(client_credentials_manager = ccm)
    return sp

def GetTrackDetails(spotifyObject, playlistURI):
    track_details = dict()
    for track in spotifyObject.playlist_tracks(playlistURI)["items"]:  
        #Track name
        track_name = track["track"]["name"]
    
        #Artist name
        artist_name = track["track"]["artists"][0]["name"]
        
        track_details[track_name] = artist_name
        # print(track_name, artist_name)
    
    return track_details

def DownloadMP3(video_URL):
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_URL, download = False)
    cwd = os.getcwd()
    filename = f"{video_info['title']}.mp3"
    outputLocation = cwd+"/spotify_songs/"+filename
    options = {'format' : 'bestaudio/best', 'keepvideo' : False, 'outtmpl' : outputLocation}

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))
    
def TryDownloadAgain(video_URL, numOfTries):
    try:
        numOfTries += 1
        DownloadMP3(video_URL = video_URL)
    except:
        if numOfTries <= 10:
            print("Trying again...")
            numOfTries += 1
            TryDownloadAgain(video_URL = video_URL, numOfTries = numOfTries)
        else:
            numOfTries = 0
            print("Too many failures...")

def main():
    # Step 1 (Get your cid and secret from spotify api website)
    cid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    secret = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
    # Authenticate without user
    sp = AuthenticationWithoutUser(cid = cid, secret = secret)
    
    myPlaylist = "https://open.spotify.com/playlist/1O3GYgbm803IfXaes7mrwW?si=e4d257582bdb4e27"
    myPlaylistURI = myPlaylist.split("/")[-1].split("?")[0]
    
    # Add track names and artist names to a list so we can use them further
    track_details = GetTrackDetails(spotifyObject = sp, playlistURI = myPlaylistURI)
    print((track_details))
    
    # Step 2
    track_links = []
    for track in track_details:
        # Example: searchQuery = The Rumbling SiM -> https://www.youtube.com/results?search_query=The+Rumbling+SiM
        searchQuery = track + " " + track_details[track]
        processedSearchQuery = searchQuery.replace(" ", "+")
        # processedSearchQuery = processedSearchQuery.encode("utf-8")
        print(processedSearchQuery)
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + quote(processedSearchQuery))
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        
        # 1st video ID should most likely be the most relevant for our use  
        video_URL = "https://www.youtube.com/watch?v=" + video_ids[0]
        print(video_URL)
        track_links.append(video_URL)
    print(track_links)
    print(len(track_links))
        
    # Step 3
    cwd = os.getcwd()
    dir = os.path.join(cwd, "spotify_songs")
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)
    
    numOfTries = 0
    for video_URL in track_links:
        TryDownloadAgain(video_URL = video_URL, numOfTries = numOfTries)
    
if __name__ == "__main__":
    main()

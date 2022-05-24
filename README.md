# Spotify-Playlist-Downloader
Download songs from your favorite playlists for free!  
 ## How to use this?
 ### Initial Setup:
 - You will need the latest version of Python installed in your computer.
 - I have put a ```requirements.txt``` which contains all the dependencies and theire versions required for this project.
 - Install the required dependencies using the command ```pip install -r requirements.txt```.

 ### Setting up Spotify API:
 - You will need a Spotify account to get access to the Spotify API, it's free.
 - Go to [Spotify for Developers](https://developer.spotify.com).
 - Go to the Dashboard section and login using your Spotify account.
 - Click on 'Create an App' give it some name and description and click on create.
 - You will be presented with an interface something like:
 ![Home Page](https://github.com/Hole0Hunter/Spotify-Playlist-Downloader/blob/main/developer.spotify.com%20home%20screen.png?raw=true)
- Your Client ID and Client Secret are important and are to be kept _SECRET_

### Setting up the code:
- In the code, put your Client ID and Client Secret in ```cid``` and ```secret``` variables respectively.
- Put the Spotify playlist link of your choice in the ```myPlaylist``` variable.

### Running the code:
- Run the code and wait for the program to fetch the details of the tracks in the playlist and wait for it to download.
- You can find a folder named ```spotify_songs``` created where the songs will downloaded to.

## Note:
- This works for playlists that are open to the public.
- This works by deploying a web crawler into youtube and downloading mp3 from the most relevant video it finds, which works most of the times. 
- There might be some instances where in a video might be restricted to some audience (age restriction etc) in which case that particular song will be skipped.

## Future Work:
I would like to spend some time fine tuning some of the features in the project like:
- Adding a command line input system for Client ID, Client Secret and Playlist link.
- Some original music videos on youtube have extra parts in the beginning and the end, to deal with that problem, adding "lyrics" at the end of the youtube search query should have better chances of eliminating the extra parts.
- At the end of a run, show the user which songs failed to download, so that the user can atleast find a manual method to download the songs.
- Please feel free to fork this project and use it for your own purposes.
- You can also open issues or suggest new features. I'll look into them. :smile:

import pandas as pd 
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from src.helpers import log, env

cid = env.get_env('SPOTIFY_CLIENT')
client_secret = env.get_env('SPOTIFY_SECRET')
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 
sp.trace=False

def get_songs_from_playlist(playlist_id):
    try:
        content_playlist = sp.playlist(playlist_id, fields=["tracks"])
        songs = content_playlist['tracks']['items']

        # Get songs by id
        songs_id = {}
        for s in songs:
            sid = s['track']['id']
            songs_id[sid] = {
                'popularity': s['track']['popularity']
            }
        return songs_id
    except Exception as e:
        log.error('get_songs_from_playlist - Not possible to get songs from playlist {playlist_id}')
        return False

def get_audio_analisys(tracks_id):
    try:
        tracks = sp.audio_features(tracks=tracks_id)
        return tracks
    except Exception as e:
        log.error('get_audio_analisys - Not possible to get track information {track_id}')
        return False

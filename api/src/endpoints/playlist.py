from flask import request, jsonify
from src.services import spotify


def generate():
    body = request.json

    # TODO: Put this on the controller
    tracks = spotify.get_songs_from_playlist(body['playlist'])
    tracks_id = tracks.keys()
    tracks_analysis = spotify.get_audio_analisys(tracks_id)
    for ta in tracks_analysis:
        tid = ta['id']
        taux = tracks[tid]
        tracks[tid] = ta
        for key, value in taux.items():
            tracks[tid][key] = value

    # Step 1: Get songs

    # Step 2: Split and remove songs from the mood lists

    # Step 3: Generate playlists

    # Step 4: Send playlists id
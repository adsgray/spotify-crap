#!/bin/env python3


# must be defined in env:
#SPOTIPY_CLIENT_ID
#SPOTIPY_CLIENT_SECRET

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_playlists(user):
    pl = sp.user_playlists(user)
    return pl

#def get_playlist_contents(playlist):
    #pl = so.playlist(playlist.id)
    #return pl


#def get_playlist_tracks(playlist):
    #tracks = so.playlist(playlist['id'], fields=


def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def print_playlist_tracks(username,playlist_id):
    tracks = get_playlist_tracks(username, playlist_id)
    for track in tracks:
        #t = json.loads(track)
        #print(t)
        #print(track['name'])
        #print(track['added_at'])
        album = track['track']['album']['name']
        try:
            artist = track['track']['album']['artists'][0]['name']
        except:
            print(track['track']['album'])
            artist="UNKNOWN"
        trackname = track['track']['name']
        print("%s,%s,%s" % (artist, album, trackname))
        #print(track)

def print_playlists(username):
    playlists = get_playlists('adsgray2000')
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name'], playlist['id']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

def print_all_playlist_tracks(username):
    playlists = get_playlists(username)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print(playlist['name'])
            print_playlist_tracks(username, playlist['id'])
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

print_all_playlist_tracks('adsgray2000')

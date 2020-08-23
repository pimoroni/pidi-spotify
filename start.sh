#!/bin/bash

cd /home/pi/pidi-spotify

export SPOTIPY_CLIENT_ID="YOUR CLIENT ID"
export SPOTIPY_CLIENT_SECRET="YOUR CLIENT SECRET"

python3 -m pidi_spotify

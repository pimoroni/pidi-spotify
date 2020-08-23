#!/bin/bash

exec >> /home/pi/spotipy/hook.log
exec 2>&1

echo "$PLAYER_EVENT track:$TRACK_ID:$POSITION_MS " 

if [ "$PLAYER_EVENT" = "start" ]; then
	echo "track:$TRACK_ID:$POSITION_MS " > /tmp/spotify_album_display
elif [ "$PLAYER_EVENT" = "change" ]; then
	echo "track:$TRACK_ID:$POSITION_MS " > /tmp/spotify_album_display
elif [ "$PLAYER_EVENT" = "playing" ]; then
	echo "seek:$POSITION_MS " > /tmp/spotify_album_display
elif [ "$PLAYER_EVENT" = "stop" ]; then
	echo "track:$TRACK_ID:$POSITION_MS " > /tmp/spotify_album_display
elif [ "$PLAYER_EVENT" = "volume_set" ]; then
	volume=$(($VOLUME * 100 / 65536))
	echo "volume:$volume" > /tmp/spotify_album_display
fi

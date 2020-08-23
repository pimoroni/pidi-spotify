# PiDi Spotify
## Pirate Display: Spotify Edition (Very, very beta)

This program has one mission: hook Raspotify to display track information and album art on a Pirate Audio board's LCD display

## Beta Notice

Right now this software is very, very beta and the method for installing/running it is expected to change very drastically.

Don't follow these instructions unless you're prepared:

* for things to break horribly in future
* to have to uninstall everything (potentially a new Pi OS image) and reinstall again to get the fixed version

*DO* follow these instructions if:

* You like to live on the bleeding edge
* You wanna see this awesomeness in action
* You'd like to contribute to how this software shapes up, find bugs and help me make it easier for future users to install and use

## Installing


### Raspotify

You've got Raspotify set up, right? Yes? No? What do you mean no? Why are you even here? Go and install Raspotify and come back when you're ready!

### Your Spotify CLIENT_ID and CLIENT_SECRET

Go to https://developer.spotify.com/dashboard and set up a new app. Grab your Client ID and Secret and keep them handy.

Remember your Client ID and Client Secret, you will need to export these into environment variables like so before running PiDi Spotify:

```
export SPOTIPY_CLIENT_ID="YOUR CLIENT ID"
export SPOTIPY_CLIENT_SECRET="YOUR CLIENT SECRET"
```

### PiDi Spotify

Install the dependencies, PiDi Spotify uses `pidi_display_st7789` and the Spotify API:

```
sudo pip3 install spotipy pidi_display_st7789
```

Grab PiDi Spotify using git, best stick it in `/home/pi` so we're working from a common path for now:

```
cd /home/pi
git clone https://github.com/pimoroni/pidi-spotify
cd pidi-spotify
```

Make super sure `hook.sh` is executable. This is the script that Raspotify uses to communicate with PiDi Spotify:

```
sudo chmod +x hook.sh
```

Now edit Raspotify's config file:

```
sudo nano /etc/default/raspotify
```

You need to add `--onevent /home/pi/pidi-spotify/hook.sh` to the `OPTIONS=` section. My options look like this, but yours might vary:

```
OPTIONS="--device hw:1,0 --onevent /home/pi/pidi-spotify/hook.sh"
```

Now, re-start Raspotify so it knows to use the hook:

```
sudo systemctl restart raspotify
```

Finally run PiDi Spotify so Raspotify can talk to it:

```
export SPOTIPY_CLIENT_ID="YOUR CLIENT ID"
export SPOTIPY_CLIENT_SECRET="YOUR CLIENT SECRET"
python3 -m pidi_spotify
```

You can copy `start.sh` to `/home/pi`, edit it and add it to crontab using `crontab -e` and adding the line `@reboot /home/pi/start.sh`. Don't check your Client ID and Secret into GitHub!


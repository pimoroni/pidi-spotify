#!/usr/bin/python3

import os
import sys
from pathlib import Path

FIFO_FILE = "/tmp/pidi-spotify.fifo"
LOG_FILE = "/tmp/pidi-spotify-hook.log"


class EventHandlers:
    def __init__(self, fifo_file):
        self.fifo_file = fifo_file

    def write(self, command):
        if Path(self.fifo_file).is_fifo():
            with open(self.fifo_file, "w") as f:
                f.write(f"{command}\n")
        else:
            print(f"Unable to write. {self.fifo_file} does not exist.")

    def dispatch(self, event, env):
        handler = getattr(self, f"event_{event}", None)
        if handler is not None:
            handler(env)
            return True
        return False

    def event_start(self, env):
        track_id = env["TRACK_ID"]
        position_ms = env.get("POSITION_MS", 0)
        self.write(f"track:{track_id}:{position_ms}")

    def event_change(self, env):
        track_id = env["TRACK_ID"]
        position_ms = env.get("POSITION_MS", 0)
        self.write(f"track:{track_id}:{position_ms}")

    def event_playing(self, env):
        track_id = env["TRACK_ID"]
        position_ms = env.get("POSITION_MS", 0)
        self.write(f"track:{track_id}:{position_ms}")

    def event_paused(self, env):
        track_id = env["TRACK_ID"]
        self.write(f"pause:{track_id}")

    def event_stop(self, env):
        track_id = env["TRACK_ID"]
        position_ms = env.get("POSITION_MS", 0)
        self.write(f"track:{track_id}:{position_ms}")

    def event_volume_set(self, env):
        volume = int(env.get("VOLUME", 0))
        volume = volume * 100 // 65535
        self.write(f"volume:{volume}")


def main(args):
    log_file = getattr(args, "hook_log_file", LOG_FILE)
    fifo_file = getattr(args, "fifo_file", FIFO_FILE)

    si = open("/dev/null", "r")
    so = open(log_file, "a+")
    se = open(log_file, "a+")

    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

    try:
        event = os.environ["PLAYER_EVENT"].lower()
    except KeyError:
        print("PLAYER_EVENT environment variable not set?")
        return 1

    eventhandlers = EventHandlers(fifo_file)
    if not eventhandlers.dispatch(event, os.environ):
        print(f"Unhandled event: {event}")
        return 1

    return 0


if __name__ == "main":
    sys.exit(main({}))

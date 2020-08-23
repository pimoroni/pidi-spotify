class Display:
    """Base class to represent a pidi display output."""

    # pylint: disable=too-many-instance-attributes
    def __init__(self, args=None):
        """Initialise a new display."""
        self._size = args.size
        self._title = ""
        self._shuffle = False
        self._repeat = False
        self._state = ""
        self._volume = 0
        self._progress = 0
        self._elapsed = 0

        self._title = ""
        self._album = ""
        self._artist = ""

    def update_album_art(self, input_file):
        """Update the display album art."""
        raise NotImplementedError

    def update_overlay(
        self, shuffle, repeat, state, volume, progress, elapsed, title, album, artist
    ):
        """Update the display transport information."""
        # pylint: disable=too-many-arguments
        self._shuffle = shuffle
        self._repeat = repeat
        self._state = state
        self._volume = volume
        self._progress = progress
        self._elapsed = elapsed
        self._title = title
        self._album = album
        self._artist = artist

    def redraw(self):
        """Redraw the display."""
        raise NotImplementedError

    def add_args(argparse):  # pylint: disable=no-self-argument
        """Expand argparse instance with display-specific args."""

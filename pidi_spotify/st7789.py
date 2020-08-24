import sys

from . import display

sys.modules["pidi.display"] = display
import pidi_display_st7789
from PIL import ImageDraw


class DisplayST7789(pidi_display_st7789.DisplayST7789):
    def __init__(self, args=None):
        pidi_display_st7789.DisplayST7789.__init__(self, args)

        # Remove the next track overlay control, since there's no way to control transport via Raspotify

        controls_pause = ImageDraw.Draw(self.controls_pause)
        controls_pause.rectangle((205, 60, 235, 80), (0, 0, 0, 0))

        controls_play = ImageDraw.Draw(self.controls_play)
        controls_play.rectangle((205, 60, 235, 80), (0, 0, 0, 0))

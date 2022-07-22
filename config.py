import pygame
import os

from sound import Sound
from theme import Theme


class Config:
    def __init__(self):
        self.themes = []
        self._add_themes()
        self.index = 0
        self.theme = self.themes[self.index]

        self.move_sound = Sound(os.path.join("assets/sounds/move.wav"))
        self.capture_sound = Sound(os.path.join("assets/sounds/capture.wav"))

    def change_theme(self):
        self.index += 1
        self.index %= len(self.themes)
        self.theme = self.themes[self.index]

    def _add_themes(self):
        green = Theme(
            (234, 235, 200),
            (119, 154, 88),
            (244, 247, 116),
            (172, 195, 51),
            (200, 100, 100),
            (200, 70, 70),
        )
        brown = Theme(
            (235, 209, 166),
            (165, 117, 80),
            (245, 234, 100),
            (209, 185, 59),
            (200, 100, 100),
            (200, 70, 70),
        )
        blue = Theme(
            (229, 228, 200),
            (60, 95, 135),
            (123, 187, 227),
            (43, 119, 191),
            (200, 100, 100),
            (200, 70, 70),
        )
        gray = Theme(
            (120, 119, 118),
            (86, 85, 84),
            (99, 126, 143),
            (82, 102, 128),
            (200, 100, 100),
            (200, 70, 70),
        )

        self.themes = [green, brown, blue, gray]

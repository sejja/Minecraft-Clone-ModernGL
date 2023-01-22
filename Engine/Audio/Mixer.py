#
#	Mixer.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 15/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import pygame

class Mixer:
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Declares an empty bank of loaded sounds
    # ------------------------------------------------------------------------
    def __init__(self):
        pygame.mixer.init()
        self.loadedsounds = {}

    # ------------------------------------------------------------------------
    # Play Sound
    #
    # Plays a sound, by id of the filename
    # ------------------------------------------------------------------------
    def PlaySound(self, soundfile, max_loops = 0):
        if not soundfile in self.loadedsounds.keys():
            n = len(self.loadedsounds)
            self.loadedsounds[soundfile] = [n, pygame.mixer.Sound(soundfile)]
        pygame.mixer.Channel(self.loadedsounds[soundfile][0]).play(self.loadedsounds[soundfile][1], loops=max_loops)

    # ------------------------------------------------------------------------
    # Pause
    #
    # Pauses an already loaded sound
    # ------------------------------------------------------------------------
    def Pause(self, soundfile):
        if soundfile in self.loadedsounds.keys():
            pygame.mixer.Channel(self.loadedsounds[soundfile][0]).pause()

audio = Mixer()
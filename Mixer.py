import pygame

class Mixer:
    def __init__(self):
        pygame.mixer.init()
        self.loadedsounds = {}

    def PlaySound(self, soundfile):
        if not soundfile in self.loadedsounds.keys():
            n = len(self.loadedsounds)
            self.loadedsounds[soundfile] = [n, pygame.mixer.Sound(soundfile)]
        pygame.mixer.Channel(self.loadedsounds[soundfile][0]).play(self.loadedsounds[soundfile][1])


audio = Mixer()
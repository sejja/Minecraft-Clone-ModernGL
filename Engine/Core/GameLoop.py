#
#	GameLoop.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 19/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import pygame
import sys
import glm
from Engine.Graphics.Basic.Light import Light
from Engine.Graphics import GraphicsPipeline

class GameLoop:
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Initializer Pygame and creates the Graphics Engine and scene
    # ------------------------------------------------------------------------
    def __init__(self):
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.set_mode((1600, 900), flags=pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        self.mDeltaTime = 0
        gfxengine = GraphicsPipeline.Gfx
        gfxengine.SetApp(self)
        gfxengine.AddLight(Light(glm.vec3(30, 30, 10)))

    # ------------------------------------------------------------------------
    # Input
    #
    # Should we quit the game=
    # ------------------------------------------------------------------------
    def Input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    # ------------------------------------------------------------------------
    # Render
    #
    # Renderices the Game, and displays it into the world
    # ------------------------------------------------------------------------
    def Present(self):
        gfxengine = GraphicsPipeline.Gfx
        gfxengine.GetContext().clear()
        gfxengine.render()
        pygame.display.flip()

    # ------------------------------------------------------------------------
    # Run
    #
    # Runs the game - game loop
    # ------------------------------------------------------------------------
    def Run(self):
        while True:
            self.Input()
            self.scene.Update()
            self.Present()
            self.mDeltaTime = pygame.time.Clock().tick(60)
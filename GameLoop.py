import pygame as pg
import sys
import glm
from Graphics.Components.Camera import Camera
from light import Light
from scene import Scene
import GraphicsPipeline
import AssetManager

class GameLoop:
    def __init__(self, win_size=(1600, 900)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # camera
        # mesh
        GraphicsPipeline.Gfx.SetApp(self)
        GraphicsPipeline.Gfx.AddLight(Light())
        # scene



    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        GraphicsPipeline.Gfx.GetContext().clear(color=(0.08, 0.16, 0.18))
        # render scene
        GraphicsPipeline.Gfx.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.scene.update()
            self.render()
            self.delta_time = self.clock.tick(60)
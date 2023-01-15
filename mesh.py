from vao import VAO
from texture import Texture
import GraphicsPipeline

class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO()
        self.texture = Texture(GraphicsPipeline.Gfx.GetContext())

    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()
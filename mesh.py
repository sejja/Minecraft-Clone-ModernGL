from Graphics.Basic.Model import Model
from texture import Texture
import GraphicsPipeline
import Carrier
import shader_program
import Graphics.Basic.VertexBuffers

class Mesh:
    def __init__(self, app):
        self.app = app
        Carrier.carry.AddContent('cube_vbo', Graphics.Basic.VertexBuffers.CubeVertexBuffer())
        Carrier.carry.AddContent('skybox_vbo', Graphics.Basic.VertexBuffers.SkyBoxVertexBuffer())
        Carrier.carry.AddContent('cube_vao', Model(shader_program.ShaderProgram(GraphicsPipeline.Gfx.GetContext()).programs['default'], Carrier.carry.GetContent('cube_vbo')))
        Carrier.carry.AddContent('shadow_cube_vao', Model(shader_program.ShaderProgram(GraphicsPipeline.Gfx.GetContext()).programs['shadow_map'], Carrier.carry.GetContent('cube_vbo')))
        Carrier.carry.AddContent('skybox_vao', Model(shader_program.ShaderProgram(GraphicsPipeline.Gfx.GetContext()).programs['advanced_skybox'], Carrier.carry.GetContent('skybox_vbo')))
        self.texture = Texture(GraphicsPipeline.Gfx.GetContext())

    def destroy(self):
        self.texture.destroy()
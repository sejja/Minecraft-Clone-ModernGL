from Graphics.Basic.Model import Model
from Graphics.Basic.Texture import Texture
import GraphicsPipeline
import Carrier
import shader_program
import Graphics.Basic.VertexBuffers

class Mesh:
    def __init__(self, app):
        self.app = app
        Carrier.carry.AddContent("shaders/default", shader_program.ShaderProgram("shaders/default"))
        Carrier.carry.AddContent("shaders/shadow_map", shader_program.ShaderProgram("shaders/shadow_map"))
        Carrier.carry.AddContent("shaders/advanced_skybox", shader_program.ShaderProgram("shaders/advanced_skybox"))
        Carrier.carry.AddContent('cube_vbo', Graphics.Basic.VertexBuffers.CubeVertexBuffer())
        Carrier.carry.AddContent('skybox_vbo', Graphics.Basic.VertexBuffers.SkyBoxVertexBuffer())
        Carrier.carry.AddContent('cube_vao', Model(Carrier.carry.GetContent("shaders/default").GetShaderObject(), Carrier.carry.GetContent('cube_vbo')))
        Carrier.carry.AddContent('shadow_cube_vao', Model(Carrier.carry.GetContent("shaders/shadow_map").GetShaderObject(), Carrier.carry.GetContent('cube_vbo')))
        Carrier.carry.AddContent('skybox_vao', Model(Carrier.carry.GetContent("shaders/advanced_skybox").GetShaderObject(), Carrier.carry.GetContent('skybox_vbo')))
        Carrier.carry.AddContent('textures/img.png', Texture('textures/img.png'))
        Carrier.carry.AddContent('textures/img_1.png', Texture('textures/img_1.png'))
        Carrier.carry.AddContent('textures/img_2.png', Texture('textures/img_2.png'))
        Carrier.carry.AddContent('textures/img_3.png', Texture('textures/img_3.png'))
        Carrier.carry.AddContent('textures/img_4.png', Texture('textures/img_4.png'))
        Carrier.carry.AddContent('textures/img_5.png', Texture('textures/img_5.png'))
        Carrier.carry.AddContent('textures/img_6.png', Texture('textures/img_6.png'))
        Carrier.carry.AddContent('textures/img_7.png', Texture('textures/img_7.png'))
        Carrier.carry.AddContent('textures/img_8.png', Texture('textures/img_8.png'))
        Carrier.carry.AddContent('textures/img_9.png', Texture('textures/img_9.png'))
        Carrier.carry.AddContent('textures/img_10.png', Texture('textures/img_10.png'))

    def Destroy(self):
        pass
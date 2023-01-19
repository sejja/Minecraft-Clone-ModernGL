import glm
import pygame
import GraphicsPipeline
from Graphics.Basic import GraphicComponent
import AssetManager
from Graphics.Basic import Model
from Graphics.Basic import VertexBuffers

class SkyboxRenderer(GraphicComponent.GraphicComponent):
    def __init__(self, owner):
        super(SkyboxRenderer, self).__init__(owner)

    def SetSkyboxBox(self, name):
        if not AssetManager.Assets.AssetExists("skybox_vao"):
            AssetManager.Assets.AddContent('skybox_vao',
                                           Model.Model(AssetManager.Assets.GetContent(
                                               "Content/Shaders/skybox.shader").GetShaderObject(),
                                                 VertexBuffers.SkyBoxVertexBuffer()))
            AssetManager.Assets.AddContent("skybox.tex", self.ProcessSkybox(name))

        self.texture = AssetManager.Assets.GetContent("skybox.tex")
        self.vao = AssetManager.Assets.GetContent("skybox_vao")
        self.vao.GetShader()['u_Texture'] = 0
        self.texture.use(location=0)

    def ProcessSkybox(self, dir_path):
        textures = []

        for x in ['right', 'left', 'top', 'bottom', 'back', 'front']:
            texture = pygame.image.load(dir_path + f'{x}.png').convert()
            if x in ['right', 'left', 'front', 'back']:
                texture = pygame.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pygame.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        texture_cube = GraphicsPipeline.Gfx.GetContext().texture_cube(
            size=textures[0].get_size(), components=3, data=None)

        for i in range(6):
            texture_data = pygame.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def Render(self):
        self.vao.GetShader()['u_mProj'].write(glm.inverse(
            GraphicsPipeline.Gfx.GetCamera().get_projection_matrix() *
            glm.mat4(glm.mat3(GraphicsPipeline.Gfx.GetCamera().get_view_matrix()))))
        super().Render()

    def Destroy(self):
        AssetManager.Assets.Destroy("skybox_vao")
        AssetManager.Assets.Destroy("skybox.tex")
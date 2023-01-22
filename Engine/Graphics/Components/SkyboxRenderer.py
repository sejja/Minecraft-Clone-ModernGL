import glm
import pygame
from Engine.Graphics import GraphicsPipeline
from Engine.Graphics.Components import GraphicComponent
from Engine.Core.Assets import AssetManager
from Engine.Graphics.Basic import VertexBuffers, Model


class SkyboxRenderer(GraphicComponent.GraphicComponent):
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Passes the owner to the base component class
    # ------------------------------------------------------------------------
    def __init__(self, owner):
        super(SkyboxRenderer, self).__init__(owner)

    # ------------------------------------------------------------------------
    # Set Skybox Box
    #
    # Given a path, scans it for textures to create an skybox texture, and Uploads
    #   to the GPU
    # ------------------------------------------------------------------------
    def SetSkyboxBox(self, path):
        if not AssetManager.Assets.AssetExists("skybox_vao"):
            AssetManager.Assets.AddContent('skybox_vao',
                                           Model.Model(AssetManager.Assets.GetContent(
                                               "Content/Shaders/skybox.shader").GetShaderObject(),
                                                       VertexBuffers.SkyBoxVertexBuffer()))
            AssetManager.Assets.AddContent("skybox.tex", self.ProcessSkybox(path))

        texture = AssetManager.Assets.GetContent("skybox.tex")
        texture.use(location=0)
        self.mVao = AssetManager.Assets.GetContent("skybox_vao")
        self.mVao.GetShader()['u_Texture'] = 0

    # ------------------------------------------------------------------------
    # Process Skybox
    #
    # Helper function that gets the texture and uploads them into Pygame
    # ------------------------------------------------------------------------
    @staticmethod
    def ProcessSkybox(dir_path):
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

    # ------------------------------------------------------------------------
    # Render
    #
    # Renders the skybox using OpenGL
    # ------------------------------------------------------------------------
    def Render(self):
        self.mVao.GetShader()['u_mProj'].write(glm.inverse(
            GraphicsPipeline.Gfx.GetCamera().GetProjectionMatrix() *
            glm.mat4(glm.mat3(GraphicsPipeline.Gfx.GetCamera().GetViewMatrix()))))
        super().Render()

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Releases the assets from the asset manager and the GPU
    # ------------------------------------------------------------------------
    def Destroy(self):
        AssetManager.Assets.Destroy("skybox_vao")
        AssetManager.Assets.Destroy("skybox.tex")
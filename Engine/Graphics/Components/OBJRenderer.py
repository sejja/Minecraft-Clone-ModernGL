#
#	OBJRenderer.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 15/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import glm
from Engine.Graphics import GraphicsPipeline
from Engine.Core.Assets import AssetManager
from Engine.Graphics.Components import GraphicComponent
from Engine.Graphics.Basic import Model

class OBJRenderer(GraphicComponent.GraphicComponent):
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Uploads the Vertices, Shaders and texture to the GPU, and initializes
    #   rendering variables
    # ------------------------------------------------------------------------
    def __init__(self, owner, model, shader, texture):
        super(OBJRenderer, self).__init__(owner)
        self.mModelMatrix = owner.mTransform.GetModelMatrix()
        vao_name = model + "_" + shader

        if not AssetManager.Assets.AssetExists(vao_name):
            AssetManager.Assets.AddContent(vao_name, Model.Model(
                AssetManager.Assets.GetContent(shader).GetShaderObject(),
                AssetManager.Assets.GetContent(model)))

        shadow_vao_name = model + "_shadow"

        if not AssetManager.Assets.AssetExists(shadow_vao_name):
            AssetManager.Assets.AddContent(shadow_vao_name, Model.Model(
                AssetManager.Assets.GetContent("Content/Shaders/shadow_map.shader").GetShaderObject(),
                AssetManager.Assets.GetContent(model)))

        camera = GraphicsPipeline.Gfx.GetCamera()

        self.mTexture = texture
        depth_texture = GraphicsPipeline.Gfx.GetDepthTexture()
        depth_texture.use(location=1)
        self.texture_ist = AssetManager.Assets.GetContent(self.mTexture)
        self.texture_ist.GetTexture().use()
        self.mVao = AssetManager.Assets.GetContent(vao_name)
        self.mShadowVao = AssetManager.Assets.GetContent(shadow_vao_name)
        self.mShader = self.mVao.GetShader()
        self.mShader['m_ViewLight'].write(GraphicsPipeline.Gfx.GetLights()[0].GetLightMatrix())
        self.mShader['u_resolution'].write(glm.vec2([1600, 900]))
        self.mShader['u_shadowmap'] = 1
        self.mShader['u_texture'] = 0
        self.shadow_program = self.mShadowVao.GetShader()
        self.shadow_program['m_Proj'].write(camera.GetProjectionMatrix())
        self.shadow_program['m_ViewLight'].write(GraphicsPipeline.Gfx.GetLights()[0].GetLightMatrix())
        self.mShader['m_Proj'].write(camera.GetProjectionMatrix())
        self.mShader['u_light.position'].write(GraphicsPipeline.Gfx.GetLights()[0].mPosition)

    # ------------------------------------------------------------------------
    # Render
    #
    # Renders the object with OpenGL
    # ------------------------------------------------------------------------
    def Render(self):
        camera = GraphicsPipeline.Gfx.GetCamera()

        self.texture_ist.GetTexture().use(location=0)
        self.mShader['u_CamPos'].write(camera.mPostition)
        self.mShader['m_View'].write(camera.GetViewMatrix())
        self.mShader['m_Model'].write(self.mModelMatrix)
        super().Render()

    # ------------------------------------------------------------------------
    # Shadow Render
    #
    # Renders the Shadows into the shadow texture
    # ------------------------------------------------------------------------
    def ShadowRender(self):
        self.shadow_program['m_Model'].write(self.mModelMatrix)
        self.mShadowVao.GetGLArrayObject().render()
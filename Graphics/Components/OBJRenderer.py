import glm
import GraphicsPipeline
import AssetManager
from Graphics.Basic import GraphicComponent
from Graphics.Basic import Model

class OBJRenderer(GraphicComponent.GraphicComponent):
    def __init__(self, owner, model, shader, tex_id):
        super(OBJRenderer, self).__init__(self)
        self.m_model = self.get_model_matrix(owner.mTransform)

        self.vao_name = model + "_" + shader

        if not AssetManager.Assets.AssetExists(self.vao_name):
            AssetManager.Assets.AddContent(self.vao_name, Model.Model(
                AssetManager.Assets.GetContent(shader).GetShaderObject(),
                AssetManager.Assets.GetContent(model)))

        self.shadow_vao_name = model + "_shadow"

        if not AssetManager.Assets.AssetExists(self.shadow_vao_name):
            AssetManager.Assets.AddContent(self.shadow_vao_name, Model.Model(
                AssetManager.Assets.GetContent(shader).GetShaderObject(),
                AssetManager.Assets.GetContent(model)))
        self.tex_id = tex_id
        self.vao = AssetManager.Assets.GetContent(self.vao_name)
        self.shadow_vao = AssetManager.Assets.GetContent(self.shadow_vao_name)
        self.program = self.vao.GetShader()
        self.on_init()

    def SetTexture(self, tex_id):
        self.tex_id = tex_id
        self.vao = AssetManager.Assets.GetContent(self.vao_name)
        self.shadow_vao = AssetManager.Assets.GetContent(self.shadow_vao_name)
        self.program = self.vao.GetShader()
        self.on_init()

    def get_model_matrix(self, transform):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, transform.mPosition)
        # rotate
        m_model = glm.rotate(m_model, transform.mRotation.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, transform.mRotation.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, transform.mRotation.x, glm.vec3(1, 0, 0))
        # scale
        m_model = glm.scale(m_model, transform.mScale)
        return m_model

    def Render(self):
        self.texture.GetTexture().use(location=0)
        self.program['camPos'].write(GraphicsPipeline.Gfx.GetCamera().position)
        self.program['m_view'].write(GraphicsPipeline.Gfx.GetCamera().m_view)
        self.program['m_model'].write(self.m_model)
        super().Render()

    def RenderShadow(self):
        self.shadow_program['m_model'].write(self.m_model)
        self.shadow_vao.GetGLArrayObject().render()

    def on_init(self):
        self.program['m_view_light'].write(GraphicsPipeline.Gfx.GetLights()[0].m_view_light)
        self.program['u_resolution'].write(glm.vec2([1600, 900]))
        self.depth_texture = GraphicsPipeline.Gfx.get_depth_texture()
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        #shadow
        self.shadow_program = self.shadow_vao.GetShader()
        self.shadow_program['m_proj'].write(GraphicsPipeline.Gfx.GetCamera().get_projection_matrix())
        self.shadow_program['m_view_light'].write(GraphicsPipeline.Gfx.GetLights()[0].m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # texture
        self.texture = AssetManager.Assets.GetContent(self.tex_id)
        self.program['u_texture_0'] = 0
        self.texture.GetTexture().use()
        # mvp
        self.program['m_proj'].write(GraphicsPipeline.Gfx.GetCamera().get_projection_matrix())
        self.program['m_view'].write(GraphicsPipeline.Gfx.GetCamera().get_view_matrix())
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(GraphicsPipeline.Gfx.GetLights()[0].position)
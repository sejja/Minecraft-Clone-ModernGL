import glm
import pygame
import AssetManager
import GraphicsPipeline
from Graphics.Basic import Model
from Graphics.Basic import VertexBuffers

class BaseModel:
    def __init__(self, app, vbo_name, shader_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.camera = self.app.camera

        vao_name = vbo_name  + "_" + shader_name

        if not AssetManager.Assets.AssetExists(vao_name):
            AssetManager.Assets.AddContent(vao_name, Model.Model(
                AssetManager.Assets.GetContent(shader_name).GetShaderObject(),
                AssetManager.Assets.GetContent(vbo_name)))

        shadow_vao_name = vbo_name + "_shadow"

        if not AssetManager.Assets.AssetExists(shadow_vao_name):
            AssetManager.Assets.AddContent(shadow_vao_name, Model.Model(
                AssetManager.Assets.GetContent("shaders/shadow_map.shader").GetShaderObject(),
                AssetManager.Assets.GetContent(vbo_name)))

        self.tex_id = tex_id
        self.vao = AssetManager.Assets.GetContent(vao_name)
        self.shadow_vao = AssetManager.Assets.GetContent(shadow_vao_name)
        self.program = self.vao.GetShader()

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.GetGLArrayObject().render()


class Cube(BaseModel):
    def __init__(self, app, tex_id, pos, rot = (0, 0, 0), scale = (1, 1, 1)):
        super().__init__(app, "Content/Meshes/Cube.obj", "shaders/default.shader",
        tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.GetTexture().use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.GetGLArrayObject().render()

    def on_init(self):
        self.program['m_view_light'].write(self.app.light.m_view_light)
        self.program['u_resolution'].write(glm.vec2([1600, 900]))
        self.depth_texture = GraphicsPipeline.Gfx.get_depth_texture()
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        #shadow
        self.shadow_program = self.shadow_vao.GetShader()
        self.shadow_program['m_proj'].write(self.camera.get_projection_matrix())
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # texture
        self.texture = AssetManager.Assets.GetContent(self.tex_id)
        self.program['u_texture_0'] = 0
        self.texture.GetTexture().use()
        # mvp
        self.program['m_proj'].write(self.camera.get_projection_matrix())
        self.program['m_view'].write(self.camera.get_view_matrix())
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)


class AdvancedSkyBox(BaseModel):
    def __init__(self, app, vao_name='skybox_vao', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):

        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.camera = self.app.camera
        self.tex_id = tex_id

        if not AssetManager.Assets.AssetExists("skybox_vao"):
            AssetManager.Assets.AddContent('skybox_vao',
                                           Model.Model(AssetManager.Assets.GetContent(
                                               "shaders/advanced_skybox.shader").GetShaderObject(),
                                                 VertexBuffers.SkyBoxVertexBuffer()))

        self.vao = AssetManager.Assets.GetContent("skybox_vao")
        self.program = self.vao.GetShader()

        self.on_init()

    def update(self):
        m_view = glm.mat4(glm.mat3(self.camera.get_view_matrix()))
        self.program['m_invProjView'].write(glm.inverse(self.camera.get_projection_matrix() * m_view))

    def on_init(self):
        # texture
        self.texture = self.get_texture_cube(self.tex_id)
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)

    def get_texture_cube(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        # textures = [pg.image.load(dir_path + f'{face}.{ext}').convert() for face in faces]
        textures = []
        for face in faces:
            texture = pygame.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pygame.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pygame.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = GraphicsPipeline.Gfx.GetContext().texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pygame.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube




















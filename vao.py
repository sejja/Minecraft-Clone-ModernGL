import Carrier
import GraphicsPipeline
from shader_program import ShaderProgram
import Graphics.Basic.Vbo

class VAO:
    def __init__(self):
        Carrier.carry.AddContent('cube_vbo', Graphics.Basic.Vbo.CubeVBO())
        Carrier.carry.AddContent('skybox_vbo', Graphics.Basic.Vbo.SkyBoxVBO())
        self.program = ShaderProgram(GraphicsPipeline.Gfx.GetContext())
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = Carrier.carry.GetContent('cube_vbo'))

        # cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=Carrier.carry.GetContent('cube_vbo'))

        # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=Carrier.carry.GetContent('skybox_vbo'))

    def get_vao(self, program, vbo):
        vao = GraphicsPipeline.Gfx.GetContext().vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.program.destroy()
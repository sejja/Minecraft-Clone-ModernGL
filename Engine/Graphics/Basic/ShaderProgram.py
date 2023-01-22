#
#	ShaderProgram.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 17/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

from Engine.Graphics import GraphicsPipeline

class ShaderProgram:
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Loads a shader, and uploads it to the GPU
    # ------------------------------------------------------------------------
    def __init__(self, shader_name):
        shaders = [".vert", ".frag"]

        for i in range(2):
            with open(shader_name + shaders[i]) as file:
                shaders[i] = file.read()
                file.close()

        self.mProgram = GraphicsPipeline.Gfx.GetContext().program(vertex_shader= shaders[0],
                                                                  fragment_shader= shaders[1])

    # ------------------------------------------------------------------------
    # Get Shader Object
    #
    # Returns the OpenGL Handle to the Shader
    # ------------------------------------------------------------------------
    def GetShaderObject(self):
        return self.mProgram

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Unloads the Shader from the GPU
    # ------------------------------------------------------------------------
    def Destroy(self):
        self.mProgram.release()
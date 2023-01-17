#
#	Vao.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 16/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import GraphicsPipeline

class Model:
    # ------------------------------------------------------------------------
    # __init__
    #
    # Constructor of the Model Class
    # ------------------------------------------------------------------------
    def __init__(self, shader, vertex_object):
        self.mVertexBuffer = vertex_object
        self.mShader = shader
        self.mVao = GraphicsPipeline.Gfx.GetContext().vertex_array(self.mShader,
            [(vertex_object.GetGLVertexBufferObject(), self.mVertexBuffer.GetFormat(),
            *self.mVertexBuffer.GetAttributes())])

    # ------------------------------------------------------------------------
    # Get OpenGL Array Object
    #
    # Returns the Vertex Array of OpenGL
    # ------------------------------------------------------------------------
    def GetGLArrayObject(self):
        return self.mVao

    # ------------------------------------------------------------------------
    # Get Shader
    #
    # Returns the shader program
    # ------------------------------------------------------------------------
    def GetShader(self):
        return self.mShader

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Releases the Vertex Buffer from the GPU
    # ------------------------------------------------------------------------
    def Destroy(self):
        self.mVertexBuffer.Destroy()
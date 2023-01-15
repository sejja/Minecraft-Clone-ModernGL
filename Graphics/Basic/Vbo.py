#
#	VBO.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 15/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import numpy as np
import GraphicsPipeline
import pywavefront

class BaseVBO:
    # ------------------------------------------------------------------------
    # __init__
    #
    # Constructor of basic Vertex Buffer Object
    # ------------------------------------------------------------------------
    def __init__(self, format, attribs):
        self.vbo = self.CreateVertexBuffer()
        self.format = format
        self.attribs = attribs

    # ------------------------------------------------------------------------
    # GetVertices
    #
    # Gets the vertices of an object - VIRTUAL
    # ------------------------------------------------------------------------
    def GetVertices(self): ...

    # ------------------------------------------------------------------------
    # Create Vertex Buffer
    #
    # Creates the Vertex Buffer of an Object in OpenGL
    # ------------------------------------------------------------------------
    def CreateVertexBuffer(self):
        return GraphicsPipeline.Gfx.GetContext().buffer(self.GetVertices())

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Releases the Vertex Buffer from the GPU
    # ------------------------------------------------------------------------
    def Destroy(self):
        self.vbo.release()

class CubeVBO(BaseVBO):
    # ------------------------------------------------------------------------
    # __init__
    #
    # Constructor of the cube Vertex Buffer Object
    # ------------------------------------------------------------------------
    def __init__(self):
        super().__init__('2f 3f 3f', ['in_texcoord_0', 'in_normal', 'in_position'])

    # ------------------------------------------------------------------------
    # Get Vertices
    #
    # Constructor of the cube Vertex Buffer Object
    # ------------------------------------------------------------------------
    def GetVertices(self):
        return np.array(pywavefront.Wavefront('Content/Meshes/cube.obj', parse=True).materials.popitem()[1].vertices, dtype='f4')

class SkyBoxVBO(BaseVBO):
    # ------------------------------------------------------------------------
    # __init__
    #
    # Constructor of the Skybox vertex object
    # ------------------------------------------------------------------------
    def __init__(self):
        super().__init__('3f', ['in_position'])

    # ------------------------------------------------------------------------
    # Get Vertices
    #
    # Returns the vertices of the Skybox
    # ------------------------------------------------------------------------
    def GetVertices(self):
        return np.array([(-1, -1, 0.9999), (3, -1, 0.9999), (-1, 3, 0.9999)], dtype='f4')
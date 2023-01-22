#
#	Importers.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 14/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import Engine.Graphics.Basic.Texture
import Engine.Graphics.Basic.ShaderProgram
from Engine.Graphics.Basic import VertexBuffers

class Importer:
    def ImportFromFile(self, name): ...


class PNGImporter(Importer):
    # ------------------------------------------------------------------------
    # Import From File
    #
    # Imports a PNG File
    # ------------------------------------------------------------------------
    def ImportFromFile(self, name):
        return Engine.Graphics.Basic.Texture.Texture(name)

class SHADERImporter(Importer):
    # ------------------------------------------------------------------------
    # Import From File
    #
    # Imports a Shader (.vert and .frag) File
    # ------------------------------------------------------------------------
    def ImportFromFile(self, name):
        return Engine.Graphics.Basic.ShaderProgram.ShaderProgram(name)

class OBJImporter(Importer):
    # ------------------------------------------------------------------------
    # Import From File
    #
    # Imports an OBJ File
    # ------------------------------------------------------------------------
    def ImportFromFile(self, name):
        return VertexBuffers.VertexBuffer3D(name)
import Graphics.Basic.Texture
import Graphics.Basic.ShaderProgram
from Graphics.Basic import VertexBuffers

class Importer:
    def ImportFromFile(self, name): ...


class PNGImporter(Importer):
    def ImportFromFile(self, name):
        return Graphics.Basic.Texture.Texture(name)

class SHADERImporter(Importer):
    def ImportFromFile(self, name):
        return Graphics.Basic.ShaderProgram.ShaderProgram(name)

class OBJImporter(Importer):
    def ImportFromFile(self, name):
        return VertexBuffers.VertexBuffer3D(name)
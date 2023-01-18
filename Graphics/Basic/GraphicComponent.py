import ECSystem
import AssetManager

class GraphicComponent(ECSystem.Component):
    def __init__(self, owner):
        super(GraphicComponent, self).__init__(owner)

    def Update(self, deltatime):
        pass

    def Render(self):
        self.vao.GetGLArrayObject().render()

    def Destroy(self):
        pass
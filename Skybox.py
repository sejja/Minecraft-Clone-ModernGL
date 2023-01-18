import ECSystem
from Graphics.Components import SkyboxRenderer

class SkyBox(ECSystem.Object):
    def __init__(self, tex_id='skybox'):
        super(SkyBox, self).__init__()
        self.mComponents.append(SkyboxRenderer.SkyboxRenderer(self))
        self.mComponents[0].SetSkyboxBox(tex_id)

    def Render(self):
        super().Render()

    def Destroy(self):
        pass
import Transform

class Entity:
    def Update(self, deltatime): ...
    def Render(self): ...

    def ShadowRender(self):
        pass
    def Destroy(self): ...

class Object(Entity):
    def __init__(self):
        self.mComponents = []
        self.mTransform = Transform.Transform()
    def Render(self):
        [x.Render() for x in self.mComponents]

    def ShadowRender(self):
        [x.ShadowRender() for x in self.mComponents]

    def Destroy(self):
        [x.Destroy() for x in self.mComponents]

class Component(Entity):
    def __init__(self, owner):
        self.mOwner = owner
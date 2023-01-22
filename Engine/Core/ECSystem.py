#
#	ECSystem.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 19/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

from Engine.Core.Math import Transform

class Entity:
    def Update(self, deltatime): ...
    def Render(self): ...

    def ShadowRender(self):
        pass
    def Destroy(self): ...

class Object(Entity):
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Creates a Transform for our object
    # ------------------------------------------------------------------------
    def __init__(self):
        self.mComponents = []
        self.mTransform = Transform.Transform()

    # ------------------------------------------------------------------------
    # Render
    #
    # Renders everyone of our components
    # ------------------------------------------------------------------------
    def Render(self):
        [x.Render() for x in self.mComponents]

    # ------------------------------------------------------------------------
    # Shadow Render
    #
    # Renders the Shadow of each component
    # ------------------------------------------------------------------------
    def ShadowRender(self):
        [x.ShadowRender() for x in self.mComponents]

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Calls the Destructor on every component
    # ------------------------------------------------------------------------
    def Destroy(self):
        [x.Destroy() for x in self.mComponents]

class Component(Entity):
    # ------------------------------------------------------------------------
    # Constructor
    #
    # Assingns our Owner Object
    # ------------------------------------------------------------------------
    def __init__(self, owner):
        self.mOwner = owner
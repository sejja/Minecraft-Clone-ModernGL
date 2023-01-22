#
#	GraphicComponent.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 15/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

from Engine.Core import ECSystem

class GraphicComponent(ECSystem.Component):
    # ------------------------------------------------------------------------
    # __init__
    #
    # Passes the Owner to the Component base class
    # ------------------------------------------------------------------------
    def __init__(self, owner):
        super(GraphicComponent, self).__init__(owner)

    # ------------------------------------------------------------------------
    # Update
    #
    # Does nothing
    # ------------------------------------------------------------------------
    def Update(self, deltatime):
        pass

    # ------------------------------------------------------------------------
    # Render
    #
    # Render the vertex array on OpenGL
    # ------------------------------------------------------------------------
    def Render(self):
        self.mVao.GetGLArrayObject().render()

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Does nothing
    # ------------------------------------------------------------------------
    def Destroy(self):
        pass
#
#	Light.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 27/12/22
#	Copyright © 2023 Deusto. All Rights reserved
#

import glm

class Light:
    # ------------------------------------------------------------------------
    # __init__
    #
    # Constructs a white light
    # ------------------------------------------------------------------------
    def __init__(self, position):
        self.mPosition = position

    # ------------------------------------------------------------------------
    # Get View Matrix
    #
    # Returns the view matrix of the light. Important for building shadowmaps
    # ------------------------------------------------------------------------
    def GetLightMatrix(self):
        return glm.lookAt(self.mPosition, glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))
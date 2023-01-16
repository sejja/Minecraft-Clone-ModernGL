#
#	Camera.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 05/01/23
#	Copyright © 2023 Deusto. All Rights reserved
#

import math
import glm
import Carrier

class Camera:
    #------------------------------------------------------------------------
    # __init__
    #
    # Constructor of the Camera
    #------------------------------------------------------------------------
    def __init__(self):
        self.mPostition = glm.vec3(0, 0, 0)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = -90
        self.pitch = 0

    # ------------------------------------------------------------------------
    # Update
    #
    # Updates the Camera Vectors
    # ------------------------------------------------------------------------
    def update(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        self.forward = glm.normalize(glm.vec3(math.cos(yaw) * math.cos(pitch),
                                math.sin(pitch),
                                math.sin(yaw) * math.cos(pitch)))
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))
        self.m_view = self.get_view_matrix()

    # ------------------------------------------------------------------------
    # Get View Matrix
    #
    # Computes the View Matrix and returns it
    # ------------------------------------------------------------------------
    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    # ------------------------------------------------------------------------
    # Get Projection Matrix
    #
    # Computes the Projection Matrix and returns it
    # ------------------------------------------------------------------------
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(50), Carrier.carry.GetWindowWidth() / Carrier.carry.GetWindowHeight(), 0.01, 5000)





















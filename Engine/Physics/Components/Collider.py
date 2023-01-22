#
#	Collider.py
#	Minecraft Clone
#
#	Created by Diego Revilla on 17/12/22
#	Copyright © 2023 Deusto. All Rights reserved
#

from Engine.Core import ECSystem
from Engine.Physics import VoxelPhysicSystem

class VoxelCollider(ECSystem.Component):
    # ------------------------------------------------------------------------
    # Construct
    #
    # Adds the Collider to the Physics System
    # ------------------------------------------------------------------------
    def __init__(self, owner):
        super(VoxelCollider, self).__init__(owner)
        VoxelPhysicSystem.Physx.AddStaticCollider(self)

    # ------------------------------------------------------------------------
    # Destroy
    #
    # Removes the Collider from the Physics System
    # ------------------------------------------------------------------------
    def Destroy(self):
        VoxelPhysicSystem.Physx.RemoveStaticCollider(self)
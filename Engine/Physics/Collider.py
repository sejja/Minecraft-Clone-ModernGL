import ECSystem
import VoxelPhysicSystem

class VoxelCollider(ECSystem.Component):
    def __init__(self, owner):
        super(VoxelCollider, self).__init__(owner)
        VoxelPhysicSystem.Physx.AddStaticCollider(self)

    def Destroy(self):
        VoxelPhysicSystem.Physx.RemoveStaticCollider(self)
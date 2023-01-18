import glm
import ECSystem
from Graphics.Components import OBJRenderer
from Engine.Physics import Collider

class Cube(ECSystem.Object):
    def __init__(self, tex_id, pos, rot = glm.vec3(0, 0, 0), scale = glm.vec3(1, 1, 1)):
        super().__init__()
        self.mTransform.mPosition = pos
        self.mTransform.mRotation = rot
        self.mTransform.mScale = scale
        self.mComponents.append(OBJRenderer.OBJRenderer(self, "Content/Meshes/Cube.obj",
            "shaders/default.shader", tex_id))
        self.mComponents.append(Collider.VoxelCollider(self))
import glm

class Transform:
    def __init__(self, position = glm.vec3(0, 0, 0), scale = glm.vec3(1, 1, 1),
        rotation = glm.vec3(0, 0, 0)):
        self.mPosition = position
        self.mScale = scale
        self.mRotation = rotation
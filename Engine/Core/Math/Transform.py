import glm

class Transform:
    def __init__(self, position = glm.vec3(0, 0, 0), scale = glm.vec3(1, 1, 1),
        rotation = glm.vec3(0, 0, 0)):
        self.mPosition = position
        self.mScale = scale
        self.mRotation = rotation

    # ------------------------------------------------------------------------
    # Get Model Matrix
    #
    # Gets the matrix of the model given a transformation
    # ------------------------------------------------------------------------
    def GetModelMatrix(self):
        model = glm.mat4()
        model = glm.translate(model, self.mPosition)
        model = glm.rotate(model, self.mRotation.x, glm.vec3(1, 0, 0))
        model = glm.rotate(model, self.mRotation.y, glm.vec3(0, 1, 0))
        model = glm.rotate(model, self.mRotation.z, glm.vec3(0, 0, 1))
        model = glm.scale(model, self.mScale)
        return model
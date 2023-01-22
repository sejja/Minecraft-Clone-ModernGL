import glm

class VoxelPhysicSystem():
    # ------------------------------------------------------------------------
    # Bresenham 3D
    #
    # Calculates shortest blocky path between two points
    # CODE FROM GEEKSFORGEEKS
    #
    # https://www.geeksforgeeks.org/bresenhams-algorithm-for-3-d-line-drawing/
    # ------------------------------------------------------------------------
    @staticmethod
    def Bresenham3D(x1, y1, z1, x2, y2, z2):
        ListOfPoints = []
        ListOfPoints.append((x1, y1, z1))
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        dz = abs(z2 - z1)
        if (x2 > x1):
            xs = 1
        else:
            xs = -1
        if (y2 > y1):
            ys = 1
        else:
            ys = -1
        if (z2 > z1):
            zs = 1
        else:
            zs = -1

        # Driving axis is X-axis"
        if (dx >= dy and dx >= dz):
            p1 = 2 * dy - dx
            p2 = 2 * dz - dx
            while (x1 != x2):
                x1 += xs
                if (p1 >= 0):
                    y1 += ys
                    p1 -= 2 * dx
                if (p2 >= 0):
                    z1 += zs
                    p2 -= 2 * dx
                p1 += 2 * dy
                p2 += 2 * dz
                ListOfPoints.append((x1, y1, z1))

        # Driving axis is Y-axis"
        elif (dy >= dx and dy >= dz):
            p1 = 2 * dx - dy
            p2 = 2 * dz - dy
            while (y1 != y2):
                y1 += ys
                if (p1 >= 0):
                    x1 += xs
                    p1 -= 2 * dy
                if (p2 >= 0):
                    z1 += zs
                    p2 -= 2 * dy
                p1 += 2 * dx
                p2 += 2 * dz
                ListOfPoints.append((x1, y1, z1))

        # Driving axis is Z-axis"
        else:
            p1 = 2 * dy - dz
            p2 = 2 * dx - dz
            while (z1 != z2):
                z1 += zs
                if (p1 >= 0):
                    y1 += ys
                    p1 -= 2 * dz
                if (p2 >= 0):
                    x1 += xs
                    p2 -= 2 * dz
                p1 += 2 * dy
                p2 += 2 * dx
                ListOfPoints.append((x1, y1, z1))
        return ListOfPoints

    def SetBounds(self, minbound3, maxbound3):
        self.min_bound = minbound3
        self.max_bound = maxbound3
        self.dimensions = maxbound3 - minbound3

    def Setup(self):
        self.collisionsgrid = [[ [False] * int(self.dimensions.z) for i in range(int(self.dimensions.y))] for j in range(int(self.dimensions.x))]

    def RaycastClosestPoint(self, position, direction):
        list_of_points = self.Bresenham3D(int(position.x),
                                     int(position.y),
                                     int(position.z),
                                     int((position.x + direction.x * 10)),
                                     int((position.y + direction.y * 10)),
                                     int((position.z + direction.z * 10)))

        for i in list_of_points:
            if self.IsColliding(glm.vec3(i[0], i[1], i[2])):
                return i

        return glm.vec3(position)

    def RaycastClosestPointInmediatePrevious(self, position, direction):
        list_of_points = self.Bresenham3D(int(position.x),
                                     int(position.y),
                                     int(position.z),
                                     int((position.x + direction.x * 10)),
                                     int((position.y + direction.y * 10)),
                                     int((position.z + direction.z * 10)))

        last_point = position

        for i in list_of_points:
            if self.IsColliding(glm.vec3(i[0], i[1], i[2])):
                return last_point
            last_point = i

        return glm.vec3(position)

    def IsColliding(self, position, direction= glm.vec3(0, 0, 0)):
        pos = glm.vec3(position.x + direction.x,position.y + direction.y, position.z + direction.z)
        return self.collisionsgrid[int(pos.x)][int(pos.y)][int(pos.z)]

    def AddStaticCollider(self, collider):
        pos = collider.mOwner.mTransform.mPosition
        self.collisionsgrid[int(pos.x)][int(pos.y)][int(pos.z)] = True

    def RemoveStaticCollider(self, collider):
        pos = collider.mOwner.mTransform.mPosition
        self.collisionsgrid[int(pos.x)][int(pos.y)][int(pos.z)] = False

Physx = VoxelPhysicSystem()
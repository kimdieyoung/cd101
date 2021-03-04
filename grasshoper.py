import math
class vector3D:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
        
    def __str__(self):
        return "X: {0}, Y: {1}, Z:{2}".format(self.X, self.Y, self.Z)
    def get_len(self):
       return math.sqrt(self.X**2 + self.Y**2 + self.Z**2)
    @staticmethod
    def dot(self, other):
        return self.X * other.X + self.Y * other.Y + self.Z * other.Z
    def cross(self, other):
        return vector3D(self.Y*other.Z - self.Z*other.Y,
        self.Z*other.X - self.X*other.Z,
        self.X*other.Y - self.Y*other.X)
    def scale(self, n):
        return vector3D(self.X * n, self.Y * n, self.Z *n)
    def sum (self, other):
        return vector3D(self.X + other.X, self.Y + other.Y, self.Z + other.Z)
    def __add__(self, other):
        return vector3D(self.X + other.X, self.Y + other.Y, self.Z + other.Z)
    def 
v1 = vector3D(10, 10, 0)
v2 = vector3D(20, 0, 0)
v3 = v1 + v2
print(v3)
a = v3.X
b = v3.Y
c = v3.Z

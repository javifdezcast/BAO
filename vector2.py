import math

class Vector2:

    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Cannot add a number to a Vector2")

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Cannot subtract a number from a Vector2")

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)  # Allow multiplication by the vector on the right side as well

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return Vector2(0, 0)
        else:
            return Vector2(self.x / magnitude, self.y / magnitude)

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def rotate(self, angle_degrees: float) -> 'Vector2':
        """Rotates this Vector2 instance around the origin (0, 0)."""

        angle_radians = math.radians(angle_degrees)
        rotated_x = self.x * math.cos(angle_radians) - self.y * math.sin(angle_radians)
        rotated_y = self.x * math.sin(angle_radians) + self.y * math.cos(angle_radians)

        return Vector2(rotated_x, rotated_y)

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

    def __repr__(self):
        return self.__class__.__name__ + "(" + ", ".join(f"{a}" for a in (self.x, self.y)) + ")"


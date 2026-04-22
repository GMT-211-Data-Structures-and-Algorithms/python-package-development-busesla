class Point:
    """Nokta geometrisi sınıfı."""
    def __init__(self, x, y, label=None):
        self.x = float(x)
        self.y = float(y)
        self.label = label

    def __repr__(self):
        return f"Point({self.label}: {self.x}, {self.y})"

class Line:
    """Çizgi geometrisi sınıfı."""
    def __init__(self, name):
        self.name = name
        self.points = []

    def add_point(self, point_obj):
        self.points.append(point_obj)

    def __repr__(self):
        return f"Line({self.name}, {len(self.points)} points)"
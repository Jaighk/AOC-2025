class Coord:
    def __init__(self, x, y, z):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.conns: list[Coord] = []

    def __repr__(self):
        string: str = f"""x: {self.x}
y: {self.y}
z: {self.z}
conns: {self.conns}"""
        return string

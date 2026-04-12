# Luhan | A data structure primarily meant to implement two-parameter coordinates
@datatype
class Coordinate:
    x: float
    y: float

    def __str__(self):
        return f"({x} , {y})"

Coord = Coordinate # type alias for easy reference

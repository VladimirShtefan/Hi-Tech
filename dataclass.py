from pydantic.dataclasses import dataclass as pyd_dataclass

from config import MAX_SUM


@pyd_dataclass(eq=True, frozen=True)
class Coordinate:
    x: int
    y: int


@pyd_dataclass(eq=True, frozen=True)
class Node:
    coordinate: Coordinate

    @property
    def neighbours(self) -> tuple:
        neighbours = []
        coordinate = Coordinate(x=self.coordinate.x - 1, y=self.coordinate.y)
        if self.coordinate.x != 0 and self.point_is_reachable(coordinate):
            neighbours.append(coordinate)

        coordinate = Coordinate(x=self.coordinate.x + 1, y=self.coordinate.y)
        if self.point_is_reachable(coordinate):
            neighbours.append(coordinate)

        coordinate = Coordinate(x=self.coordinate.x, y=self.coordinate.y - 1)
        if self.coordinate.y != 0 and self.point_is_reachable(coordinate):
            neighbours.append(coordinate)

        coordinate = Coordinate(x=self.coordinate.x, y=self.coordinate.y + 1)
        if self.point_is_reachable(coordinate):
            neighbours.append(coordinate)

        return tuple(neighbours)

    @staticmethod
    def get_weight(coordinate: Coordinate) -> int:
        return sum([int(num) for num in ''.join(map(str, (coordinate.x, coordinate.y)))])

    def point_is_reachable(self, coordinate) -> bool:
        return self.get_weight(coordinate) <= MAX_SUM

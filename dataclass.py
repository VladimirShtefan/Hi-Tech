from pydantic.main import BaseModel
from pydantic.dataclasses import dataclass as pyd_dataclass


@pyd_dataclass(eq=True, frozen=True)
class Coordinate:
    x: int
    y: int


@pyd_dataclass(eq=True, frozen=True)
class Node:
    coordinate: Coordinate
    weight: int


class NeighboursNodes(BaseModel):
    neighbours: list[Node, ...] | None

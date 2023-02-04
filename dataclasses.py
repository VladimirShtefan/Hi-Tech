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


class Edge(BaseModel):
    start_point: Node
    end_point: Node


class FieldGraph(BaseModel):
    field_nodes: tuple[Node]
    field_edges: tuple[Edge]


class NeighboursNodes(BaseModel):
    neighbours: list[Node, ...] | None

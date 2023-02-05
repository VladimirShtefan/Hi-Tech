from networkx import Graph

from config import START_POINT
from dataclass import Node, Coordinate


class Field:
    def __init__(self, x: int, y: int):
        self.start_point: Coordinate = Coordinate(x=x, y=y)
        self.max_sum = 25
        self.g = Graph()

    def create_start_node(self) -> None:
        """
        Для установки начальной вершины (узла)
        """
        self.g.add_node(Node(coordinate=self.start_point))

    def search_nodes(self) -> int:
        """
        Поиск всех доступных вершин с учетом доступности координат при прохождении через них
        :return: количество доступных связанных координат
        """
        self.create_start_node()
        offset = 0
        while True:
            actual_nodes = list(self.g.nodes)
            nodes_count = len(actual_nodes)
            if nodes_count == offset:
                break
            for node in actual_nodes[offset:]:
                neighbours = Node(coordinate=node.coordinate).neighbours
                for neighbour in neighbours:
                    new_node = Node(coordinate=neighbour)
                    self.g.add_node(new_node)
                    self.g.add_edge(new_node, node)
            offset = nodes_count
        return len(self.g.nodes)


if __name__ == '__main__':
    field = Field(*START_POINT)
    print(field.search_nodes())

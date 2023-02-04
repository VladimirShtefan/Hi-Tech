from networkx import Graph

from dataclass import Node, Coordinate, NeighboursNodes


class Field:
    def __init__(self, x: int, y: int):
        self.start_point: Coordinate = Coordinate(x=x, y=y)
        self.max_sum = 25
        self.g = Graph()

    def create_start_node(self) -> None:
        """
        Для установки начальной вершины (узла)
        """
        target: Node = Node(coordinate=self.start_point, weight=self.sum_digits_in_coordinates(self.start_point))
        self.g.add_node(target)

    def get_neighbours_node(self, node: Node) -> NeighboursNodes:
        """
        Для формирования соседних доступных узлов
        :param node: текущий узел
        :return: соседние узлы
        """
        neighbours = NeighboursNodes(neighbours=[])

        up_coordinates = Coordinate(x=node.coordinate.x - 1, y=node.coordinate.y)
        if node.coordinate.x != 0 and self.point_is_reachable(up_coordinates):
            neighbours.neighbours.append(Node(coordinate=up_coordinates, weight=node.weight - 1))

        down_coordinates = Coordinate(x=node.coordinate.x + 1, y=node.coordinate.y)
        if self.point_is_reachable(down_coordinates):
            neighbours.neighbours.append(Node(coordinate=down_coordinates, weight=node.weight + 1))

        left_coordinates = Coordinate(x=node.coordinate.x, y=node.coordinate.y - 1)
        if node.coordinate.y != 0 and self.point_is_reachable(left_coordinates):
            neighbours.neighbours.append(Node(coordinate=left_coordinates, weight=node.weight - 1))

        right_coordinates = Coordinate(x=node.coordinate.x, y=node.coordinate.y + 1)
        if self.point_is_reachable(right_coordinates):
            neighbours.neighbours.append(Node(coordinate=right_coordinates, weight=node.weight + 1))

        return NeighboursNodes(neighbours=neighbours.neighbours)

    def sum_digits_in_coordinates(self, coordinates: Coordinate) -> int:
        """
        Для подсчета суммы цифр в координатах
        :param coordinates: координаты
        :return: сумма цифр в координатах
        """
        return self.sum_digits(''.join(map(str, (coordinates.x, coordinates.y))))

    @staticmethod
    def sum_digits(number: str) -> int:
        return sum([int(num) for num in number])

    def point_is_reachable(self, coordinates: Coordinate) -> bool:
        """
        Проверка на доступность координаты в соответствии с max_sum
        :param coordinates: координаты
        :return: координаты или при недоступности None
        """
        return self.sum_digits_in_coordinates(coordinates) <= self.max_sum

    def search_nodes(self):
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
                for cell in self.get_neighbours_node(node).neighbours:
                    if cell:
                        self.g.add_node(cell)
                        self.g.add_edge(cell, node)
            offset = nodes_count
        return len(self.g.nodes)


if __name__ == '__main__':
    field = Field(1000, 1000)
    print(field.search_nodes())

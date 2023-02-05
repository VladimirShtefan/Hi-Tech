from networkx import Graph

from config import START_POINT, MAX_SUM


class Field:
    def __init__(self, x: int, y: int):
        self.start_point: tuple[int, int] = x, y
        self.g = Graph()

    def create_start_node(self) -> None:
        """
        Для установки начальной вершины (узла)
        """
        target = *self.start_point, self.sum_digits_in_coordinates(self.start_point)
        self.g.add_node(target)

    def get_neighbours_node(self, node: tuple[int, int, int]) -> dict:
        """
        Для формирования соседних доступных узлов
        :param node: текущий узел
        :return: соседние узлы
        """
        x, y, weight = node
        up = (x - 1, y,  weight - 1) if x != 0 else None
        down = (x + 1, y,  weight + 1)
        left = (x, y - 1, weight - 1) if y != 0 else None
        right = (x, y + 1, weight + 1)
        return {
            'up': self.point_is_reachable(up),
            'down': self.point_is_reachable(down),
            'left': self.point_is_reachable(left),
            'right': self.point_is_reachable(right),
        }

    def sum_digits_in_coordinates(self, coordinates: tuple[int, int]) -> int:
        """
        Для подсчета суммы цифр в координатах
        :param coordinates: координаты
        :return: сумма цифр в координатах
        """
        return self.sum_digits(''.join(map(str, coordinates)))

    @staticmethod
    def sum_digits(number: str) -> int:
        return sum([int(num) for num in number])

    def point_is_reachable(self, coordinates: tuple[int, int, int] | None) -> tuple | None:
        """
        Проверка на доступность координаты в соответствии с max_sum
        :param coordinates: координаты
        :return: координаты или при недоступности None
        """
        if coordinates:
            x, y, weigth = coordinates
            if self.sum_digits_in_coordinates((x, y)) <= MAX_SUM:
                return coordinates
        return None

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
                for cell in self.get_neighbours_node(node).values():
                    if cell:
                        self.g.add_node(cell)
                        self.g.add_edge(cell, node)
            offset = nodes_count
        return len(self.g.nodes)


if __name__ == '__main__':
    field = Field(*START_POINT)
    print(field.search_nodes())

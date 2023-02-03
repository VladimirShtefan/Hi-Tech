## Задание
На бесконечной координатной сетке находится муравей. Муравей может перемещается на 1 клетку вверх (x,y+1), вниз (x,y-1), влево (x-1,y), вправо (x+1,y), по одной клетке за шаг. Клетки, в которых сумма цифр в координате X плюс сумма цифр в координате Y больше чем 25 недоступны муравью. Например, клетка с координатами (59, 79) недоступна, т.к. 5+9+7+9=30, что больше 25. Сколько cклеток может посетить муравей если его начальная позиция (1000,1000), (включая начальную клетку). Прислать ответ и решение в виде числа клеток и исходного текста программы на языке Python решающей задачу.

Проект использует следующие технологии:

- [Networkx](https://networkx.org/) - NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

## Installation
Клонируйте репозиторий:
```bash
git clone https://github.com/VladimirShtefan/Hi-Tech.git
```
Настройте окружение:
```sh
# для активации окружения
poetry shell
```
```sh
# для первичной установки
poetry install
```
```sh
# для обновления
poetry update
```
Запустите проект:
```sh
# для запуска приложения
python grid.py
```
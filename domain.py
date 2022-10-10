import texttable
from texttable import Texttable


class Board:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._data = []
        for i in range(9):
            self._data.append([0]*9)

    def get_data(self):
        return self._data

    def get_grid(self, x, y):
        return self._data[x][y]

    def __str__(self):
        t = Texttable()
        # 0 for empty grid
        # 1 for *
        # 2 for E
        # 3 for grid where B cruiser is placed, but it is shown as an empty grid since cheat code hasn't been entered
        # 4 for grid where B cruiser is placed, cheat code having been entered.
        d = {0: ' ',
             1: '*',
             2: 'E',
             3: ' ',
             4: 'B'}
        row = [' ']
        for i in range(1, 9):
            row.append(i)
        t.add_row(row)
        for i in range(1, 9):
            row = self._data[i][:]  # copy of the initial list
            row[0] = chr(64 + i)
            for j in range(1, 9):
                row[j] = d[row[j]]
            t.add_row(row)
        return t.draw()


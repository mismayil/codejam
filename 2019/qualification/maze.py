# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.north = None if i == 0 and j != 0 else ''
        self.west = None if j == 0 and i != 0 else ''

    # def __repr__(self):
    #     return f'({self.i}, {self.j}) North: {self.north}, West: {self.west}'


def solve(n, footprints):
    maze = [[Cell(i, j) for j in range(n)] for i in range(n)]

    k = 0
    m = 0

    for fp in footprints:
        if fp == 'E':
            m += 1
            maze[k][m].west = None
        else:
            k += 1
            maze[k][m].north = None

    for i in range(n):
        for j in range(n):
            cell = maze[i][j]
            
            # print(f'cell: {cell}')
            
            if cell.west is not None and j-1 >= 0:
                west_cell = maze[i][j-1]
                # print(f'west cell: {west_cell}')

                if west_cell.west is not None:
                    cell.west = west_cell.west + 'E'
                elif west_cell.north is not None:
                    cell.west = west_cell.north + 'E'
                else:
                    cell.west = None

            if cell.north is not None and i-1 >= 0:
                north_cell = maze[i-1][j]
                # print(f'north cell: {north_cell}')

                if north_cell.north is not None:
                    cell.north = north_cell.north + 'S'
                elif north_cell.west is not None:
                    cell.north = north_cell.west + 'S'
                else:
                    cell.north = None
            # print(f'new cell: {cell}')

    southeast = maze[n-1][n-1]

    if southeast.north is not None:
        return southeast.north

    return southeast.west



t = int(input())

results = []

for i in range(t):
    n = int(input())
    fp = input()

    results.append('Case #{}: {}'.format(i+1, solve(n, fp)))

print('\n'.join(results))

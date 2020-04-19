# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

GO_EAST = 'go_east'
GO_SOUTH = 'go_south'

class PathError(Exception):
    pass

def go_east(from_pos, lydia, path):
    nextpos = (from_pos[0], from_pos[1]+1)
    conflict = lydia.get(from_pos)

    if nextpos[1] < n and nextpos != conflict:
        return nextpos, path + 'E'

    raise PathError

def go_south(from_pos, lydia, path):
    nextpos = (from_pos[0]+1, from_pos[1])
    conflict = lydia.get(from_pos)

    if nextpos[0] < n and nextpos != conflict:
        return nextpos, path + 'S'

    raise PathError

def solve(n, footprints):
    lydia = {}

    k = 0
    m = 0

    for fp in footprints:
        if fp == 'E':
            lydia[(k, m)] = (k, m+1)
            m += 1
        else:
            lydia[(k, m)] = (k+1, m)
            k += 1

    pos = (0, 0)
    strategy = GO_EAST
    path = ''

    if lydia.get((n-2, n-1)) is not None:
        strategy = GO_SOUTH

    while True:
        if pos == (n-1, n-1):
            return path

        if strategy == GO_EAST:
            try:
                pos, path = go_east(pos, lydia, path)
            except PathError:
                pos, path = go_south(pos, lydia, path)
        else:
            try:
                pos, path = go_south(pos, lydia, path)
            except PathError:
                pos, path = go_east(pos, lydia, path)

t = int(input())

results = []

for i in range(t):
    n = int(input())
    fp = input()

    results.append('Case #{}: {}'.format(i+1, solve(n, fp)))

print('\n'.join(results))
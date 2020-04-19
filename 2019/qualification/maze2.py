# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.north = None if x == 0 and y != 0 else ''
        self.west = None if y == 0 and x != 0 else ''


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

    start_node = Node(0, 0)
    nodes = [start_node]

    while True:
        node = nodes.pop()
        conflict = lydia.get((node.x, node.y))
        
        if node.x+1 < n:
            pos = (node.x+1, node.y)
            
            if pos != conflict:
                nextnode = Node(node.x+1, node.y)
                if node.north is not None and len(node.north) == (node.x+node.y):
                    nextnode.north = node.north + 'S'
                else:
                    nextnode.north = node.west + 'S'

                if (nextnode.x, nextnode.y) == (n-1, n-1):
                    if len(nextnode.north) == 2*n-2:
                        return nextnode.north
                    return nextnode.west
                nodes.append(nextnode)
        
        if node.y+1 < n:
            pos = (node.x, node.y+1)
            
            if pos != conflict:
                nextnode = Node(node.x, node.y+1)
                if node.north is not None and len(node.north) == (node.x+node.y):
                    nextnode.west = node.north + 'E'
                else:
                    nextnode.west = node.west + 'E'
                # print(f'nextnode: {nextnode}')
                if (nextnode.x, nextnode.y) == (n-1, n-1):
                    if len(nextnode.north) == 2*n-2:
                        return nextnode.north
                    return nextnode.west
                nodes.append(nextnode)


t = int(input())

results = []

for i in range(t):
    n = int(input())
    fp = input()

    results.append('Case #{}: {}'.format(i+1, solve(n, fp)))

print('\n'.join(results))
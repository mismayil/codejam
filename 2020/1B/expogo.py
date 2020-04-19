# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62
import math

def is_possible(x, y, j):
  s = abs(x)+abs(y)

  if s == 0:
    return False

  power = math.floor(math.log(s, 2))
  jumps = 2 ** power

  return jumps <= j

def jump(x, y, j, path):
  if j == 1:
    if x > 0:
      if (x-j, y) == (0, 0):
        return (True, 'E' + path)
    else:
      if (x+j, y) == (0, 0):
        return (True, 'W' + path)
    
    if y > 0:
      if (x, y-j) == (0, 0):
        return (True, 'N' + path)
    else:
      if (x, y+j) == (0, 0):
        return (True, 'S' + path)
    
    return (False,)

  xr = None
  yr = None

  if x > 0:
    if is_possible(x-j, y, int(j/2)):
      xr = jump(x-j, y, int(j/2), 'E' + path)
  else:
    if is_possible(x+j, y, int(j/2)):
      xr = jump(x+j, y, int(j/2), 'W' + path)

  if y > 0:
    if is_possible(x, y-j, int(j/2)):
      yr = jump(x, y-j, int(j/2), 'N' + path)
  else:
    if is_possible(x, y+j, int(j/2)):
      yr = jump(x, y+j, int(j/2), 'S' + path)

  if xr is not None and yr is not None and xr[0] and yr[0]:
    if len(xr[1]) > len(yr[1]):
      return yr
    
    return xr

  if xr is not None and xr[0]:
    return xr
  
  if yr is not None and yr[0]:
    return yr
  
  return (False,)

def solve(x, y):
  power = math.floor(math.log(abs(x)+abs(y), 2))
  jumps = 2 ** power
  result = jump(x, y, jumps, '')
  
  if not result[0]:
    return 'IMPOSSIBLE'

  return result[1]

T = int(input())
outputs = []

for t in range(T):
  x, y = [int(s) for s in input().split(' ')]
  path = solve(x, y)
  outputs.append('Case #{}: {}'.format(t+1, path))

print('\n'.join(outputs))

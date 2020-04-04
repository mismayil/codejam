# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f
def solve(s):
  sp = ''
  # number of open parenthesis
  op = 0
  lastd = None

  for c in s:
    d = int(c)
    r = d-op
    sp += '(' * r
    if r > 0:
      op += r

    if lastd is not None and d != lastd:
      if r < 0:
        sp += ')' * abs(r) + c
        op += r
      else:
        sp += c
    else:
      sp += c
    
    lastd = d
    
  sp += ')' * op

  return sp

T = int(input())
outputs = []

for t in range(T):
  s = input()
  
  sp = solve(s)
  outputs.append('Case #{}: {}'.format(t+1, sp))

print('\n'.join(outputs))
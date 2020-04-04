# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9
def solve(n, times):
  times = sorted(times, key=lambda t: t[0])

  jend = None
  cend = None
  schedule = []

  for time in times:
    st = time[0]
    et = time[1]

    if jend == None or st >= jend:
      jend = et
      schedule.append((time[2], 'J'))
    elif cend == None or st >= cend:
      cend = et
      schedule.append((time[2], 'C'))
    else:
      return 'IMPOSSIBLE'
  
  return ''.join([s[1] for s in sorted(schedule, key=lambda x: x[0])])

T = int(input())
outputs = []

for t in range(T):
  n = int(input())
  times = []

  for i in range(n):
    s = input()
    times.append(([int(e) for e in s.split(' ')] + [i]))

  a = solve(n, times)
  outputs.append('Case #{}: {}'.format(t+1, a))

print('\n'.join(outputs))
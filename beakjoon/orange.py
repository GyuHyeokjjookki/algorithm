import sys
import math

input = sys.stdin.readline

def calcStarDust(base,combo,c,skill,s):
  result = math.floor(base * (1 + (combo * c) / 100) * (1 + (skill * s) / 100))
  return result

N, K, C, R = map(int, input().split())
combo = 0
starDust = 0
skill = []
fatigue = 0

for i in range(K):
  skill.append(0)

base = input().split()

for i in range(K) :
  base[i] = int(base[i])

s = input().split()

for i in range(K):
  s[i] = int(s[i])

p = input().split()

for i in range(K):
  p[i] = int(p[i])

for i in range(N):
  l = int(input())
  if(l == 0):
    combo = 0
    if fatigue >= 100:
      continue
    elif fatigue < R:
      fatigue = 0
    else:
      fatigue -= R
    continue
  starDust += calcStarDust(base[l - 1], combo, C, skill[l - 1], s[l - 1])
  skill[l - 1] += 1
  combo += 1
  fatigue += p[l - 1]
  if(fatigue >= 100):
    starDust = -1


print(starDust)
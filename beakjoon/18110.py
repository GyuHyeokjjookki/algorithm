#방법1

import sys

sis = sys.stdin.readline
si = int(sis())

diff = []

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
if si:
    diff = [int(sis()) for _ in range(si)]
    diff.sort()
    rnd = round2(si * 0.15)
    result = diff[rnd : si - rnd]
    print(round2(sum(result) / len(result)))
else:
    print(0)

#방법2

import sys

sis = sys.stdin.readline
si = int(sis())

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

diff = []
sum = 0
if si:
    for _ in range(si):
        a = int(sis())
        diff.append(a)
    diff.sort()
    rnd = round2(si * 0.15)

    for i in range(rnd, si - rnd):
        sum += diff[i]

    print(round2(sum / (si - (rnd * 2))))
else:
    print(0)
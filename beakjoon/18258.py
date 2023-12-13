import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

queue = deque()

for _ in range(t):
    command = input().split()

    if command[0] == 'push':
        queue.append(command[1])
    if command[0] == 'front':
        if(len(queue) != 0):
            front = queue.popleft()
            queue.appendleft(front)
            print(front)
        else:
            print(-1)
    if command[0] == 'back':
        if(len(queue) != 0):
            back = queue.pop()
            queue.append(back)
            print(back)
        else:
            print(-1)
    if command[0] == 'size':
        print(len(queue))
    if command[0] == 'empty':
        if(len(queue) == 0):
            print(1)
        else:
            print(0)
    if command[0] == 'pop':
        if(len(queue) != 0):
            print(queue.pop())
        else:
            print(-1)

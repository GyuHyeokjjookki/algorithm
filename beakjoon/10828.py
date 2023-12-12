import sys
input = sys.stdin.readline
t = int(input())

arr = []

for i in range(t):
    command = input().split()
    if command[0] == 'push':
        arr.append(command[1])
    if command[0] == 'top':
        if(len(arr) > 0):
            print(arr[len(arr) - 1])
        else:
            print(0)
    if command[0] == 'pop':
        if(len(arr) > 0 ):
            print(arr.pop())
        else:
            print(-1)
    if command[0] == 'size':
        print(len(arr))
    if command[0] == 'empty':
        if len(arr) != 0:
            print(0)
        else:
            print(1)
        
import sys
sis = sys.stdin.readline
result = 1
num_list = list(map(int, sis().split()))
for i in range(len(num_list)):
    result *= num_list[i]
print(round(result/8/1024/1024,1),"MB") 
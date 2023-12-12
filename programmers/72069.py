from itertools import permutations

def check(x):
    if x < 2 :
        return False
    for i in range(2,x):
            if x % i == 0:
                return False
    return True

def solution(numbers):
    answer = []
    numbers = list(numbers)
    num = []
    
    for i in range(1, len(numbers) + 1):
        num.append(list(permutations(numbers,i)))
    num = [int(''.join(y)) for x in num for y in x]
    
    for i in num:
        if(check(i)):
            answer.append(i)
    
    return len(set(answer))

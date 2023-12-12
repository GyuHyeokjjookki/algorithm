import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    word = input()
    _word = list(word)
    answer = "YES"
    for i in range(len(_word) - 1):
        if(_word[i] == '('): stack.append(word[i])
        elif(len(stack) != 0 and _word[i] == ')' and stack[-1] == '('): stack.pop()
        else:
            answer = "NO"
            break

    if len(stack) != 0 :
        answer = "NO"
    print(answer)

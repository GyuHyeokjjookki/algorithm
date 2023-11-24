def solution(my_string):
    return ''.join(sorted(my_string.lower()))

#Test
str = "Python"

print(solution(str))
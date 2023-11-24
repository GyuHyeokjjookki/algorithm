#1
def solution(my_string, overwrite_string, s):
    my_string = list(my_string)
    my_string[s:len(overwrite_string)+s] = overwrite_string
    answer = ''.join(my_string)
    return answer


#2
def solution2(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]


my_string = "Program29b8UYP"
overwrite_string = "merS123"

print(solution(my_string, overwrite_string, 7))
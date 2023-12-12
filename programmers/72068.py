def solution(brown, yellow):
    answer = []
    max = brown + yellow
    
    for n in range(3, int(max ** 0.5) + 1):
        if max % n != 0:
            continue
        m = max // n
        if (m - 2) * (n - 2) == yellow:
            return [m,n]

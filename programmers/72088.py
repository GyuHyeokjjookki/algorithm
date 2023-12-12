def solution(triangle):
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]
    for i in range(2, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == (len(triangle[i]) - 1):
                triangle[i][j] += triangle[i-1][j - 1]
            else:
                triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j - 1], triangle[i][j] + triangle[i - 1][j])
    
            
    return max(triangle[len(triangle)-1])

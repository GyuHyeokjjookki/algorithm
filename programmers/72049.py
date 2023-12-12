def solution(n):
    triangle = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    number = 1
    
    for i in range(n):
        for j in range(i, n):
            
            if i % 3 == 0:
                x += 1
                
            elif i % 3 == 1:
                y += 1
                
            else:
                x -= 1
                y -= 1
                
            triangle[x][y] = number
            number += 1
            
    
        
    for i in range(n):
        for j in range(i + 1):
            answer.append(triangle[i][j])
        
    return answer  

                

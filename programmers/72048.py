def solution(rows, columns, queries):
    answer = []

    arr = [[0] * (columns) for _ in range(rows)]
    one = 1
    for i in range(rows):
        for j in range(columns):
                arr[i][j] += one
                one += 1
                
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = (x1 - 1), (y1 - 1), (x2 - 1), (y2 - 1)
        tmp = arr[x1][y1]
        min_value = tmp
        
        #left
        for k in range(x1, x2):
            arr[k][y1] = arr[k+1][y1]
            min_value = min(min_value, arr[k+1][y1])
            
        #bottom
        for k in range(y1, y2):
            arr[x2][k] = arr[x2][k+1]
            min_value = min(min_value, arr[x2][k+1])
            
        #right
        for k in range(x2, x1, -1):
            arr[k][y2] = arr[k-1][y2]
            min_value = min(min_value, arr[k-1][y2])
        
        #top
        for k in range(y2, y1 + 1, -1):
            arr[x1][k] = arr[x1][k-1]
            min_value = min(min_value, arr[x1][k-1])
            
        arr[x1][y1+1] = tmp
        answer.append(min_value)
    
    return answer

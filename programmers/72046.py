def solution(line):
    star = []
    for i in range(len(line)):
        for j in range(len(line)):
            x1, y1, c1 = line[i]
            x2, y2, c2 = line[j]
            if x1 * y2 == x2 * y1:
                continue
            x, y = (y1 * c2 - c1 * y2) / (x1 * y2 - y1 * x2), (x2 * c1 - x1 * c2) / (x1 * y2 - x2 * y1)
            if x.is_integer() and y.is_integer():
                x, y = int(x), int(y)
                if (x,y) not in star:
                    star.append((x,y))
                    
    min_y, max_y = star[0][1], star[0][1]
    
    for i in range(len(star)):
            if(min_y > star[i][1]):
                min_y = star[i][1]
            if(max_y < star[i][1]):
                max_y = star[i][1]
        
    max_x, min_x = max(star)[0], min(star)[0]

    arr = [['.'] * (abs(max_x - min_x + 1)) for _ in range(abs(max_y - min_y) + 1)]
    
    for s in star:
        a, b = s
        x, y = abs(max_y - b), abs(min_x - a)
        arr[x][y] = '*'
        
    for i,v in enumerate(arr):
        arr[i] = ''.join(v)
        
    return arr
def box_set(n, w, index, direction):
    a = []
    
    if(direction == 0):
        for i in range(index, w+index):
            if(i > n):
                a.append(0)
                continue
            a.append(i)
    
    if(direction == 1):
        for i in range(w+index-1, index-1, -1):
            if(i > n):
                a.append(0)
                continue
            a.append(i)
            
    return a
    
def check_box(box, num):
    target = num
    
    index = next((i, j) for i, row in enumerate(box) for j, val in enumerate(row) if val == target)
    
    answer = []
    for i in range(index[0], len(box)+1):
        try:
            if box[i][index[1]] == 0:
                break
            answer.append(box[i][index[1]])
        except IndexError:
            return answer
    return answer
    
    
def solution(n, w, num):
    index = 1
    box = []
    m = n // w
    direction = 0
    
    if(m != n/w): #가중치
        m += 1
        
    for i in range(m): #박스 설정
        box.append(box_set(n, w, index, direction))
        index += w
        if(direction == 0):
            direction = 1
        else:
            direction = 0
            
    answer = check_box(box, num)
            
    return len(answer)
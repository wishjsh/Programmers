def solution(board, h, w):
    answer = 0
    
    try:
        if(board[h][w] == board[h+1][w]):
            answer+=1
    except:
        pass
    
    
    try:
        if(board[h][w] == board[h][w+1]):
            answer+=1
    except:
        pass
    
    
    try:
        if(h-1 >= 0):
            if(board[h][w] == board[h-1][w]):
                answer+=1
    except:
        pass
    
    
    try:
        if(w-1 >= 0):
            if(board[h][w] == board[h][w-1]):
                answer+=1
    except:
        pass
    
    
    
    return answer
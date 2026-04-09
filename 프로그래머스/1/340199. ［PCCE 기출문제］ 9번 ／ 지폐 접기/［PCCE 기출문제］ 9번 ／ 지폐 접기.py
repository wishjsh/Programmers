def solution(wallet, bill):
    count = 0
    debug = []
    while(True):
        if(wallet[0] >= bill[0] and wallet[1] >= bill[1]): #안돌렸을때
            break
        
        if(wallet[1] >= bill[0] and wallet[0] >= bill[1]): #돌렸을때
            break
            
        if(bill[0] > bill[1]):
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        
        debug.append([bill[0], bill[1]])
            
        count += 1
        
    
    return count
def blank(x, y, mats, park):
    for h in range(y, y+mats):
        for w in range(x, x+mats):
            
            if(park[h][w] != "-1"):
                return 0
            
    return 1


def solution(mats, park): #브루트포스
    mats.sort(reverse=True)
    
    height = len(park) 
    weight = len(park[0])
    
    for i in mats:
        
        for h in range(height):
            for w in range(weight):
                
                if(park[h][w] == "-1"):
                    
                    if(w + i > weight or h + i > height):
                        continue
                        
                    if(blank(w, h, i, park)):
                        return i
    
    return -1
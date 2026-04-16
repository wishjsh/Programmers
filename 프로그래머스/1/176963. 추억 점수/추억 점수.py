def solution(name, yearning, photo):
    answer = []
    result = 0
    for i in photo:
        for j in i:
            for h in name:
                if(j == h):
                    result += yearning[name.index(h)]
                    break
        answer.append(result)
        result = 0
        
                
    return answer
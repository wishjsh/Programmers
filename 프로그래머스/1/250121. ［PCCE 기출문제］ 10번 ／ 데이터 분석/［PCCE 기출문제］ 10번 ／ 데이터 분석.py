def sort_ext(data, sort_by):
    if(sort_by == "code"):
        data.sort(key=lambda x: x[0])
    if(sort_by == "date"):
        data.sort(key=lambda x: x[1])
    if(sort_by == "maximum"):
        data.sort(key=lambda x: x[2])
    if(sort_by == "remain"):
        data.sort(key=lambda x: x[3])

    return data

def check(data, val_ext):
    if(data < val_ext):
        return data
    else:
        return 0

def separation(data, ext, val_ext):
    
    result = []
    
    for a, b, c, d in data:
        if(ext == "code"):
            if(check(a, val_ext)): result.append([a, b, c, d])
        if(ext == "date"):
            if(check(b, val_ext)): result.append([a, b, c, d])
        if(ext == "maximum"):
            if(check(c, val_ext)): result.append([a, b, c, d])
        if(ext == "remain"):
            if(check(d, val_ext)): result.append([a, b, c, d])
    
    return result


def solution(data, ext, val_ext, sort_by):
    answer = sort_ext(separation(data, ext, val_ext), sort_by)
    
    
    
    
    
    return answer
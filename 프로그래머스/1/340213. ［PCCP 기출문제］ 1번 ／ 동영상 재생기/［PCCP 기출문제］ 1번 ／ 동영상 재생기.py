def m2s(time):
    a = int(time[:2]) * 60
    b = int(time[3:])
    return a + b


def solution(video_len, pos, op_start, op_end, commands):
    time = m2s(op_end) if(m2s(op_start) <= m2s(pos) <= m2s(op_end)) else m2s(pos)
    
    video_s = m2s(video_len)
    
    for i in commands:
        if(i == "prev"):
            if(time - 10 <= 0):
                time = 0
            else:
                time -= 10
                
            if(m2s(op_start) <= time <= m2s(op_end)):
                time = m2s(op_end)
                
        elif(i == "next"):
            if(time + 10 >= video_s):
                time = video_s
            else:
                time += 10
                
            if(m2s(op_start) <= time <= m2s(op_end)):
                time = m2s(op_end)
    
    return f"{str(time//60).zfill(2)}:{str(time%60).zfill(2)}"
        
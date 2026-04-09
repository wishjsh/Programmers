def time1(s_time):
    hour = s_time // 100 #시
    try:
        minutes = s_time % 100 #분
    except ZeroDivisionError:
        minutes = 0
        
    return hour*60 + minutes
    
    

def check(s_time ,e_time, startday):
        for i in e_time:
            if(time1(i) <= time1(s_time) + 10 or startday in [6,7]):
                pass
            else:
                return 0
            startday += 1
            if(startday > 7):
                startday -= 7
        return 1
        


def solution(schedules, timelogs, startday):
    n = [0 for _ in range(len(schedules))]
    c = 0
    while(True):
        try:
            if(check(schedules[c], timelogs[c], startday)):
                n[c] = 1
            c += 1
        except:
            break
            
    return n.count(1)
def heal(hp, time, s2hp, p2hp, maxhp, time_now):
    if(hp <= 0):
        return -1
    
    hp += s2hp
    if(time_now == time):
        hp += p2hp
    
    if(hp >= maxhp):
        hp = maxhp
    
    return hp
    
def attack(attacks, time):
    for a, b in attacks:
        if(a == time):
            return b
        
    return 0

def solution(bandage, health, attacks):
    hp = health
    now_time = 0
    time_hp = bandage[0]
    s2hp = bandage[1]
    plus2hp = bandage[2]
    
    for i in range(attacks[-1][0]):
        at = attack(attacks, i+1)
        if(at):
            hp -= at
            now_time = 0
            continue
        
        now_time += 1
        hp = heal(hp, time_hp, s2hp, plus2hp, health, now_time)
        
        if(now_time >= time_hp):
            now_time = 0
        
        if(hp <= 0):
            break
        
    if(hp <= 0):
        return -1
    return hp
            
            
        
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def yj(signal, t):
    g, y, r = signal
    cycle = g + y + r
    pos = (t-1)%cycle
    return g <= pos < g + y

def solution(signals):
    
    total_cycle = 1
    for g, y, r in signals:
        cycle = g + y + r
        total_cycle = lcm(total_cycle, cycle)
        
    for t in range(1, total_cycle+1):
        if all(yj(signal, t) for signal in signals):
            return t
        
    return -1
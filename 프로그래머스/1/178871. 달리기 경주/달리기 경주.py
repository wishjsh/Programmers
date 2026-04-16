def change(players, index, pos_map):
    players[index], players[index-1] = players[index-1], players[index]
    
    pos_map[players[index]] = index
    pos_map[players[index-1]] = index-1

def solution(players, callings):
    
    pos_map = {player: i for i, player in enumerate(players)} # 인덱싱 O(1)
    
    for i in callings:
        change(players, pos_map[i], pos_map)
        
    return players
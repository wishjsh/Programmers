def solution(message, spoiler_ranges):
    # 1. 스포일러 구간에 해당하는 인덱스를 빠르게 참조하기 위해 Set으로 변환
    # (또는 크기가 20,000인 Boolean 리스트 사용)
    spoiler_indices = [False] * len(message)
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            spoiler_indices[i] = True
    
    # 2. 메시지를 단어 단위로 쪼개고, 각 단어의 위치(인덱스)를 추적
    words = message.split()
    spoiler_word_set = set()
    normal_word_set = set()
    
    current_idx = 0
    for word in words:
        # split()된 단어가 실제 message의 어디서 시작하는지 찾음
        start_pos = message.find(word, current_idx)
        end_pos = start_pos + len(word) - 1
        
        # 단어의 인덱스 중 하나라도 spoiler_indices에 포함되는지 확인
        is_this_spoiler = False
        for i in range(start_pos, end_pos + 1):
            if spoiler_indices[i]:
                is_this_spoiler = True
                break
        
        if is_this_spoiler:
            spoiler_word_set.add(word)
        else:
            normal_word_set.add(word)
            
        # 다음 단어 검색을 위해 인덱스 업데이트
        current_idx = end_pos + 1

    # 3. 차집합 연산: 스포일러 영역에만 등장한 고유 단어 추출
    # spoiler_word_set에만 있고 normal_word_set에는 없는 단어들
    important_words = spoiler_word_set - normal_word_set
    
    return len(important_words)
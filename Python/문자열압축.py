
def solution(src):
    answer = " "
    count = 0 # 연속하는 문자개수
    # 앞문자가 1이면 answer에 1 저장
    if src[0] == '1':
        answer += '1'
    # 문자변화를 체크하여 연속된 문자개수 answer에 저장
    for i in range(len(src)-1):
        if src[i] != src[i+1]:
        # 문자연속이 끝났으므로 압축실행 & count 갱신
            answer += chr(ord('A') + count)
            count = 0
        else:
            count += 1 # 문자가 연속되므로 count 변수증가
    answer += chr(ord('A') + count) # 마지막문자 저장
    return answer
import sys
import queue

def solution(m, n, picture):
    num_of_area = 0
    max_size_of_one_area = 0

    dx = [0,0,-1,+1]
    dy = [-1,+1,0,0]
    # 좌표를 넣을 큐 생성
    que = queue.Queue()

    # m*n 모든 칸을 이중 for문을 이용해 방문
    for i in range(m) :
         for j in range(n) :
            # 이미 방문한 칸이거나 방문한 칸이 색칠되어 있지 않으면 넘어감
            if picture[i][j] == 0 : 
                continue
            # 아직 방문하지 않았다면
            else :
                num_of_area +=1     # 영역의 개수 +1
                count = 0           # 해당 영역의 넓이 변수 초기화
                que.put((i, j))     # 큐에 해당 칸의 좌표를 push
                color = picture[i][j]   # 해당 영역의 색 저장
                picture[i][j] = 0       # 방문체크. 하지 않으면 무한 루프 돎.

                # 큐에 있는 칸들에 대해 상하좌우 검사. 큐에 원소가 없을 때까지 반복
                while que.qsize() > 0 : 
                    count += 1          # 해당 영역의 넓이 +1
                    x, y = que.get()    # 큐의 앞에 있는 좌표 pop
                    
                    for k in range(4) :     # 좌표의 범위를 확인해야함. 아니면 인덱스 오류 발생
                        # 인접한 칸 중에 같은 색을 가진 칸을 큐에 넣고 해당 칸의 색을 0으로 바꿔서 방문체크
                        if (0<= x+dx[k] < m) and (0 <= y+dy[k] < n) and (picture[x+dx[k]][y+dy[k]] == color) :
                            que.put((x+dx[k], y+dy[k]))
                            picture[x+dx[k]][y+dy[k]] = 0       # 방문체크
                max_size_of_one_area = max(max_size_of_one_area, count)     # 최댓값(넓이) 갱신
    
    return [num_of_area, max_size_of_one_area]
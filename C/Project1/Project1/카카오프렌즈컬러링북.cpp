// 컴파일 오류가 자꾸 난다...

#include <stdio.h>
#include <malloc.h>
#define max(x,y) ((x>y)? x: y)

// 좌표를 저장할 구조체
typedef struct Cord
{
	int x, y;
}Cord;


//BFS(너비우선탐색)를 위해 원형 큐 구현
//큐를 선형으로 구현할 경우 큐의 사이즈를 초과하여 사용할 수 없기 때문에 원형으로 구현.
//초과한  인덱스는 사이즈로 모듈러 연산을 하여 배열의 공간 재사용
typedef struct QueueType {
	int front, rear, size;
	// front: 큐의 첫번째 요소. pop했을 때 나올 원소의 인덱스
	// rear: 큐에 새로운 원소가 들어갈 인덱스
	Cord* Queue;		// 좌표 배열
}QueueType;


// 큐를 초기화하는 함수
void init(QueueType* q, int size) {
	q->Queue = (Cord*)malloc(sizeof(Cord) * size);		// 큐 크기만큼 동적할당
	q->front = 0;
	q->rear = 0;
	q->size = size;
}

int isEmpty(QueueType* q) {
	// 원형 큐에서 front == rear인 경우, 큐가 비었다고 봄
	return q->rear % q->size == q->front % q->size;
}

void push(QueueType* q, int x, int y) {
	// 원형 큐에서 front == rear+1 일 경우, 큐가 다 찼다고 가정. 따라서 구분을 위해 항상 한 자리는 비워둬야 함.
	if (q->rear + 1 % q->size == q->front % q->size) 
		return;		// 큐가 다 찼으면 push하지 않고 리턴 (이런 일이 없도록 처음부터 큐의 길이를 필요한 공간보다 최소 한 자리 이상 크게 잡아야 함)
	Cord c = { x, y };
	q->Queue[q->rear % q->size] = c;
	q->rear = (q->rear + 1) % q->size;		// 0<= index < size를 유지해야 함. 모듈러 연산을 잊으면 잘못된 인덱스 값에 접근하게 됨.
	return;
}

void pop(QueueType* q) {
	q->front = (q->front + 1) % q->size;		// 0<= index < size를 유지해야 함. 모듈러 연산을 잊으면 잘못된 인덱스 값에 접근하게 됨.
}

int* solution(int m, int n, int** picture) {
	int* answer = (int*)malloc(sizeof(int) * 2);
	int i, j, k;
	int number_of_area = 0, max_size_of_one_area = 0;
	int color, count, x, y;
	int dx[] = { 0,0,-1,1 };
	int dy[] = { -1,1,0,0 };
	int queue_size = m * n + 1;		// 큐에 한 번에 들어갈 수 있는 원소의 수는 그림의 크기인 m * n. 여기에 원형 큐 특성상 필요한 추가 한 자리를 더한 크기를 지정
	QueueType que;
	init(&que, queue_size);
	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j++) {
			if (picture[i][j] == 0) continue;
			else {
				number_of_area++;		// 영역의 개수 +1
				count = 0;		// 해당 영ㅇ역의 넓이 변수 초기화
				push(&que, i, j);
				color = picture[i][j];		// 해당 영역의 색을 저장
				picture[i][j] = 0;		// 방문체크 <- 하지 않으면 무한 루프
				while (!isEmpty(&que)) {
					count++;		// 해당 영역의 넓이 +1
					x = que.Queue[que.front].x;
					y = que.Queue[que.front].y;
					pop(&que);
					for (k = 0; k < 4; k++) {
						// 새로 방문할 좌표의 범위가 0<= x+dx[k] < m, 0<= y+dy[k] < n 임을 확인해야 함
						// 그림의 가장자리에 있는 칸의 경우, 상하좌우 모두를 방문할 수 없음
						if (x + dx[k] >= 0 && x + dx[k] < m && y + dy[k] >= 0 && y + dy[k] < n && picture[x + dx[k]][y + dy[k]] == color) {
							push(&que, x + dx[k], y + dy[k]);
							picture[x + dx[k]][y + dy[k]] = 0;		// 방문체크
						}
					}
				}
				max_size_of_one_area = max(max_size_of_one_area, count);		// 최댓값(넓이) 갱신
			}
		}
	}
	answer[0] = number_of_area;
	answer[1] = max_size_of_one_area;
	return answer;
}
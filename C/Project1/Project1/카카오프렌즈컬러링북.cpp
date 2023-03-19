// ������ ������ �ڲ� ����...

#include <stdio.h>
#include <malloc.h>
#define max(x,y) ((x>y)? x: y)

// ��ǥ�� ������ ����ü
typedef struct Cord
{
	int x, y;
}Cord;


//BFS(�ʺ�켱Ž��)�� ���� ���� ť ����
//ť�� �������� ������ ��� ť�� ����� �ʰ��Ͽ� ����� �� ���� ������ �������� ����.
//�ʰ���  �ε����� ������� ��ⷯ ������ �Ͽ� �迭�� ���� ����
typedef struct QueueType {
	int front, rear, size;
	// front: ť�� ù��° ���. pop���� �� ���� ������ �ε���
	// rear: ť�� ���ο� ���Ұ� �� �ε���
	Cord* Queue;		// ��ǥ �迭
}QueueType;


// ť�� �ʱ�ȭ�ϴ� �Լ�
void init(QueueType* q, int size) {
	q->Queue = (Cord*)malloc(sizeof(Cord) * size);		// ť ũ�⸸ŭ �����Ҵ�
	q->front = 0;
	q->rear = 0;
	q->size = size;
}

int isEmpty(QueueType* q) {
	// ���� ť���� front == rear�� ���, ť�� ����ٰ� ��
	return q->rear % q->size == q->front % q->size;
}

void push(QueueType* q, int x, int y) {
	// ���� ť���� front == rear+1 �� ���, ť�� �� á�ٰ� ����. ���� ������ ���� �׻� �� �ڸ��� ����־� ��.
	if (q->rear + 1 % q->size == q->front % q->size) 
		return;		// ť�� �� á���� push���� �ʰ� ���� (�̷� ���� ������ ó������ ť�� ���̸� �ʿ��� �������� �ּ� �� �ڸ� �̻� ũ�� ��ƾ� ��)
	Cord c = { x, y };
	q->Queue[q->rear % q->size] = c;
	q->rear = (q->rear + 1) % q->size;		// 0<= index < size�� �����ؾ� ��. ��ⷯ ������ ������ �߸��� �ε��� ���� �����ϰ� ��.
	return;
}

void pop(QueueType* q) {
	q->front = (q->front + 1) % q->size;		// 0<= index < size�� �����ؾ� ��. ��ⷯ ������ ������ �߸��� �ε��� ���� �����ϰ� ��.
}

int* solution(int m, int n, int** picture) {
	int* answer = (int*)malloc(sizeof(int) * 2);
	int i, j, k;
	int number_of_area = 0, max_size_of_one_area = 0;
	int color, count, x, y;
	int dx[] = { 0,0,-1,1 };
	int dy[] = { -1,1,0,0 };
	int queue_size = m * n + 1;		// ť�� �� ���� �� �� �ִ� ������ ���� �׸��� ũ���� m * n. ���⿡ ���� ť Ư���� �ʿ��� �߰� �� �ڸ��� ���� ũ�⸦ ����
	QueueType que;
	init(&que, queue_size);
	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j++) {
			if (picture[i][j] == 0) continue;
			else {
				number_of_area++;		// ������ ���� +1
				count = 0;		// �ش� �������� ���� ���� �ʱ�ȭ
				push(&que, i, j);
				color = picture[i][j];		// �ش� ������ ���� ����
				picture[i][j] = 0;		// �湮üũ <- ���� ������ ���� ����
				while (!isEmpty(&que)) {
					count++;		// �ش� ������ ���� +1
					x = que.Queue[que.front].x;
					y = que.Queue[que.front].y;
					pop(&que);
					for (k = 0; k < 4; k++) {
						// ���� �湮�� ��ǥ�� ������ 0<= x+dx[k] < m, 0<= y+dy[k] < n ���� Ȯ���ؾ� ��
						// �׸��� �����ڸ��� �ִ� ĭ�� ���, �����¿� ��θ� �湮�� �� ����
						if (x + dx[k] >= 0 && x + dx[k] < m && y + dy[k] >= 0 && y + dy[k] < n && picture[x + dx[k]][y + dy[k]] == color) {
							push(&que, x + dx[k], y + dy[k]);
							picture[x + dx[k]][y + dy[k]] = 0;		// �湮üũ
						}
					}
				}
				max_size_of_one_area = max(max_size_of_one_area, count);		// �ִ�(����) ����
			}
		}
	}
	answer[0] = number_of_area;
	answer[1] = max_size_of_one_area;
	return answer;
}
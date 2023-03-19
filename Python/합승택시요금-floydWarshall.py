import sys

INF = 1e7
# 최대 n-1 개의 간선을 지나게 됨
def fillGraph(n, fares):
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0 # 자기 자신과의 비용은 0
    for u, v, w in fares: # a->b 와 b->a 의 비용이 같은 양방향 그래프
        graph[u][v] = w
        graph[v][u] = w

    return graph

def floydWarshall(graph, n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1): # i->j와 i->k->j 중 더 적은 비용으로 갱신
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def solution(n, s, a, b, fares):
    answer = INF
    graph = fillGraph(n, fares) #초기화
    floydWarshall(graph, n) # 플로이드-워셜 적용

    for i in range(1, n+1):
        # s에서 출발해서 i까지 합승 후, 따로따로 i부터 a까지, i부터 b까지 가는 최소 택시비용
        # 최소비용(s->i) + 최소비용(i->a) +최소비용(i->b) 이 최소값일 때 최소비용이 됨
        # 이어진 경로가 없는 경우(INF)는 min 조건에 의해 자동으로 고려되지 않음
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     n,s,a,b = map(int, input().split())

#     i = 9;
#     fares=[list(map(int, input().split())) for _ in range(i)]
#     answer = solution(n,s,a,b, fares)
#     print(answer)
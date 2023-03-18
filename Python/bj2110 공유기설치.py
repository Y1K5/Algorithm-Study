#import math.sys
#input = sys.stdin.readline

n, c = map(int, input().split())
a=[int(input()) for i in range(n)]
a.sort()
start,end = 1, a[n-1]-a[0]
# 집 사이의 최소 거리, 최대 거리
result = 0

if c == 2:
    print(a[n-1] - a[0])
    # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
else:
    while(start < end):
        mid = (start + end)//2

    count = 1
    ts = a[0]
    # 마지막으로 설치된 공유기의 위치
    for i in range(n):
        if a[i] - ts >= mid:
            count += 1
            ts = a[i]
        if count >= c :
            result = mid
            start = mid + 1
        elif count < c:
            end = mid
print(result)
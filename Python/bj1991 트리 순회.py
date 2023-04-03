import sys
 
N = int(sys.stdin.readline().strip())
tree = {}
 
for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
 
# 전위 순회는 루트->왼쪽 자식->오른쪽 자식 순서로 순회
# 재귀함수 순서도 똑같이 루트 출력문, 왼쪽 재귀함수, 오른쪽 재귀함수
def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # 함수 안의 재귀함수에서 tree[root][0]는 왼쪽으로 끝까지 탐색한다는 의미
        preorder(tree[root][1])  # 함수 안의 재귀함수에서 tree[root][1]는 오른쪽으로 끝까지 탐색한다는 의미
 

# 중위 순회는 왼쪽 자식->루트->오른쪽 자식 순서로 탐색하므로
# 재귀 함수 순서도 왼쪽 재귀함수, 루트 출력문, 오른쪽 재귀함수
def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


# 후위 순회는 왼쪽 자식->오른쪽 자식->루트 순서이므로 
# 재귀 함수 순서도 왼쪽 재귀함수, 오른쪽 재귀함수, 루트 출력문 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')
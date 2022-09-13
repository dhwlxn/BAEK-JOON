import sys
input = sys.stdin.readline


def preorder(n):
    if n != '.':
        print(n, end="")
        preorder(tree[n][0])
        preorder(tree[n][1])


def inorder(n):
    if n != '.':
        inorder(tree[n][0])
        print(n, end="")
        inorder(tree[n][1])


def postorder(n):
    if n != '.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n, end="")


V = int(input().rstrip())         # 정점 개수
tree = {}
for i in range(V):
    data, l, r = input().split()
    tree[data] = (l, r)

root = 'A'
preorder(root)
print()
inorder(root)
print()
postorder(root)
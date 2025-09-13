N, M = map(int, input().split())
a = []
# 0~N까지 반복
for n in range(N):
  # a[]에 1~N까지 삽입
  a.append(n+1)
# print(a)
for m in range(M):
  i, j = map(int, input().split())
  a[i-1], a[j-1] = a[j-1], a[i-1]
for i in range(N):
  print(a[i], end=" ")
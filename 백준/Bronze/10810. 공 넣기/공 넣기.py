N,M = map(int, input().split())
a=[0 for _ in range(N)]
for _ in range(M):
  i,j,k = map(int, input().split())
  for b in range(i, j+1):
    a[b-1] = k
for i in range(N):
  print(a[i], end=" ")
cnt = 0
N = int(input())
a = list(map(int, input().split()))
V = int(input())
for j in range(0, N, 1):
  if(a[j] == V):
    cnt += 1
print(cnt)
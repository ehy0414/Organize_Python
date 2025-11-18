N = int(input())
result = 0
papers = [[0] * 100 for _ in range(100)]
for _ in range(N):
  x1, y1 = map(int, input().split())
  x2, y2 = x1+10, y1+10
  
  for i in range(x1, x2):
    for j in range(y1, y2):
      papers[i][j] = 1

for k in range(100):
  result += papers[k].count(1)

print(result)

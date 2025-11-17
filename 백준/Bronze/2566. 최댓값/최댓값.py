A, B = [], []
for row in range(9):
  row = list(map(int, input().split()))
  A.append(row.index(max(row))+1)
  B.append(max(row))

print(max(B))
print((B.index(max(B))+1), A[(B.index(max(B)))])
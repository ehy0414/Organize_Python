X = int(input())
N = int(input())
total = 0
c= []
for i in range(1,N+1,1):
  a,b = map(int, input().split())
  c.append(a*b)
for j in range(0,N,1):
  total += c[j]
if(total == X):
  print("Yes")
else:
  print("No")
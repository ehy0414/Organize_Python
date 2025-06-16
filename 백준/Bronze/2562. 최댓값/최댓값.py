b=[]
for i in range(9):
  a = int(input())
  b.append(a)
print(max(b))
print((int(b.index(max(b)))+1))
B = 42
c= []
for _ in range(10):
  A = int(input())
  result = A % B
  c.append(result)
print(len(set(c)))
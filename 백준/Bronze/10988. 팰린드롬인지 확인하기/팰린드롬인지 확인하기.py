a = str(input())
result = 0
for i in range(len(a)):
  if(a[i] == a[-i-1]):
    result = 1
  else:
    result = 0
    break
print(result)
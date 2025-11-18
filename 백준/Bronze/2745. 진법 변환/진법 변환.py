N, B = list(map(str, input().split()))
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0
for i in range(len(N)):
  result += num_list.index(N[-(i+1)]) * (int(B) ** i)
print(result)
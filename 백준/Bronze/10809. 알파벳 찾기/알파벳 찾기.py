S = input()
alpha = [chr(c) for c in range(97,123)]
result=[]
for i in range(len(alpha)):
  result.append(S.find(alpha[i]))
print(*result)
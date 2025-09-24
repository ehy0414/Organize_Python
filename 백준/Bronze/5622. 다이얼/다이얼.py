S = input()
time = 0
for i in range(len(S)):
  if(ord(S[i]) <= 90 and ord(S[i]) >= 87):
    time += 10
  elif(ord(S[i]) <= 86 and ord(S[i]) >= 84):
    time += 9
  elif(ord(S[i]) <= 83 and ord(S[i]) >= 80):
    time += 8
  elif(ord(S[i]) <= 79 and ord(S[i]) >= 77):
    time += 7
  elif(ord(S[i]) <= 76 and ord(S[i]) >= 74):
    time += 6
  elif(ord(S[i]) <= 73 and ord(S[i]) >= 71):
    time += 5
  elif(ord(S[i]) <= 70 and ord(S[i]) >= 68):
    time += 4
  elif(ord(S[i]) <= 67 and ord(S[i]) >= 65):
    time += 3
  else:
    time += 0
print(time)
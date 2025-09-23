N = int(input())
P = ""
for _ in range(N):
  R, S = map(str, input().split())
  for i in range(len(S)):
    P += S[i]*int(R)
  print(P)
  P = ""

chess = [1,1,2,2,2,8]
a, b, c, d, e, f = map(int, input().split())
chess_white = [a, b, c, d, e, f]
for i in range(len(chess)):
  chess[i] -= chess_white[i]
print(*chess)
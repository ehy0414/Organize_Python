s = input().upper()
s_list = list(set(s))
cnt = []

for i in s_list:
  s_cnt = s.count(i)
  cnt.append(s_cnt)

if cnt.count(max(cnt)) > 1:
  print("?")
else:
  print(s_list[(cnt.index(max(cnt)))])
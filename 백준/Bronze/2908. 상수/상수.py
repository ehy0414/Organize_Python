one, two = map(str, input().split())
one = one[::-1]
two = two[::-1]
print(max(int(one),int(two)))
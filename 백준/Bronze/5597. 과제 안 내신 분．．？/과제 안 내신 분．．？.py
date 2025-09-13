students = [n+1 for n in range(30)]
for i in range(28):
  n = int(input())
  students.remove(n)
students.sort()
print(*students)
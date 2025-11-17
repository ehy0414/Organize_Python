grade_score = 0
total_grade = 0
total_score = 0
for i in range(20):
  # score = 학점 grade = 과목평점
  name, score, grade =  map(str, input().split())
  if(grade == "A+"):
    grade_score = 4.5
  elif(grade == "A0"):
    grade_score = 4.0
  elif(grade == "B+"):
    grade_score = 3.5
  elif(grade == "B0"):
    grade_score = 3.0
  elif(grade == "C+"):
    grade_score = 2.5
  elif(grade == "C0"):
    grade_score = 2.0
  elif(grade == "D+"):
    grade_score = 1.5
  elif(grade == "D0"):
    grade_score = 1.0
  elif(grade == "F"):
    grade_score = 0
  else:
    continue
  total_score = total_score + float(score) # 학점
  total_grade = total_grade + (float(score) * float(grade_score))
if(total_grade == 0):
  print(total_grade)
else:
  print(total_grade / total_score)
#old style
print('%s학생의 %s 과목 성적은 %s입니다' % (student, subject, subjects[subject]))
#modern style
print("{0}학생의 {1} 과목 성적은 {2}입니다".format(student, subject, subjects[subject]))
#f스트링
print(f'{student}학생의 {subject} 과목 성적은 {subjects[subject]}입니다')
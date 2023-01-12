#(100°F − 32) × 5/9 = 37.778°C
fahrenheit = float(input('화씨온도 : '))
celsius = (fahrenheit - 32.0)*(5.0/9.0)
print(f'화씨 온도 {fahrenheit}도는 섭씨 온도 {celsius}도입니다')

#교재 countdown
countdown_list = [5,4,3,2,1,"hey!"]
for countdown in countdown_list:
    print(countdown)
print(countdown_list[-2])
print("프로그램 종료")

#교재 dictionary
subjects = {"의영": "A+",
             "전산제도": "B+",
             "유체역학": "A0"
             }
student = input("이름 : ")
subject = "유체역학"
print(student,"학생의 ",subject,"성적은",subjects["유체역학"],"입니다")

#old style
print('%s학생의 %s 과목 성적은 %s입니다' % (student, subject, subjects[subject]))
#modern style
print("{0}학생의 {1} 과목 성적은 {2}입니다".format(student, subject, subjects[subject]))
#f스트링
print(f'{student}학생의 {subject} 과목 성적은 {subjects[subject]}입니다')
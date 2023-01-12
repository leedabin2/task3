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
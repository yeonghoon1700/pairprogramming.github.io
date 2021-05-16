	# 9498번 문제

score = int(input())
if 100 >= score >= 90:
    print('A')
elif 89 >= score >= 80:
    print('B')
elif 79 >= score >= 70:
    print('C')
elif 69 >= score >= 60:
    print('D')
else:
    print('F')

    # 2753번 문제 

year = int(input())

if ((year%4 == 0) and (year%100 != 0) or (year%400 == 0)):
    print('1')
else:
    print('0')

    # 2884번 문제

H,M =map(int,input("알람 설정할 시간을 입력하세요").split())

if M > 44:
    print(H,M-45)
elif M < 45 and H > 0:
    print(H-1,M+15)
else:
    print(23,M+15)

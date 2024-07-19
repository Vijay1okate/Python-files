
'''marks ==== grade
100 to 75 = Grade A
60 to 75 === Grade b
35 to 60 ===grade c
0 to 35 === grade d'''

marks =float(input('Enter the marks'))

if marks<100 and marks>=75:
    print('Grade A')
elif marks<75 and marks>=60:
    print('Grade B')
elif marks<60 and marks>=35:
    print('Grade C')
elif marks<35 and marks>=0:
    print('Grade D')
else :
    print('Enter Valid Number')


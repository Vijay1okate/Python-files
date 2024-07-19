'''
Write a program to find the grade of the student based on the marks:

Marks    Grade
100-75   A
75-60    B
60-35    C
35-0     D

'''

marks = float(input('Enter your marks: '))

if marks<=100 and marks>=75:
    print('Grade A')
elif marks<75 and marks>=60:
    print('Grade B')
elif marks<60 and marks>=35:
    print('Grade C')
elif marks<35 and marks>=0:
    print('Grade D')
else:
    print('Enter invalid marks')

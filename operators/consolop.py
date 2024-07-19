'''
code editor ------print()==== > console(output screen)

If there is need to bring user input from output screen or console to the code editor or to store in variable ,
we need input() function.

syntax:

        variable=input()

step1: Give message to user   ==>print()
step2: store that input into variable=> var-=input()
'''

print('Enter first number:')
x=input()
print(type(x))
a=int(x)
print(type(a))

print('Enter the second number :')
y=input()
b=int(y)

z=a+b
print('Addition of ',x, 'and',y, 'is :' ,z)
    
'''#print('value of x is :',x)
print('Enter the second number :')
y=input()
print('Enter the second number :')
y=input())'''

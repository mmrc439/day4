"""
while loop
============
init variable
while condition:
    statement
    step

"""

x=1 #initialize x to 0
while x<=50:
    print(x,end='\t')
    # x=x+1
    x+=5 #compound assignment operator

#Display only even numbers from 1 to 60
i=1
while i<=60:
    if i%2==0:
        print(i,end=' ')
    i+=1

print('\n\n')

y=65
while y<=90:
    print(chr(y),end='\t')
    y+=1

print('\n\n')

y=97
while y<=122:
    print(chr(y),end='\t')
    y+=1

n=int(input('\nenter a number :'))
num=n
revnumber=0
while n!=0:
    remainder=n%10
    revnumber=revnumber*10+remainder
    n=n//10


print(f'the reverse number is {revnumber}')
if num==revnumber:
    print('the number is palindrome')
else:
    print('the number is not palindrome')

# x=0
# while x<=50:
#     print('_',end='')
#     x+=1

print('#'*60)

# 4!=4x3x2x1
fact=1
num=int(input('please enter a number :'))
if num>=0:
    x=1
    while x<=num:
        fact=fact*x
        x=x+1
    print(f'the factorial of {num} is :{fact}')
else:
    print('Sorry, the number is -ve. Please try again later.')

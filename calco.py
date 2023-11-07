# This is a program for basic math operations
# by Junior Atilang
# atthewarrior@gmail.com


#here we output a message and prompt the user to enter the first and second
#number with an operation

import math # this lib will permit us to perform mathematical tasks like sqrt

print('hello i am a calculator for all basic arithmetic calculations ')
print('I can solve any question with the following arithmetic operations ')
print('basic operations(addition,substraction,division,multiplication) advanced operations(root of a number,square of a number) ')

choice=(input('what type of operation do you want to carry. basic or advanced ?:'))

if choice=='basic':
 x=int(input('enter your first number:'))
 y=int(input('enter your second number:'))
 z=input('what operation do you want to carry?:')
else:
    a=int(input('enter a number to perform an advanced math operation like root(rt),squareroot(**), etc:'))
    z=input('what operation do you want to carry?:')

##
#here we use a switch statement to choose only an operation to carry out


# we could also use and if else statement

#be careful with the spacing you give out
#python uses identation 
if z=='+':
    result=x+y
elif z=='-':
    result=x-y
elif z=='*':
    result=x*y
elif z=='/':
    result=x/y
    result=round(result,2)
elif z=='**':
    answer=a*a
elif z=='rt':
    answer=math.sqrt(a)   
else:
    print('the operation you entered is not recognised')

if (z=='+') or (z=='-') or (z=='/') or (z=='*'):
     print(x,z,y,':',result)
elif (z=='**') or (z=='rt'):
    print('answer:',answer)
    
else:
        print('the operation you entered is not recognised or you made a mistake please try again')
    

def calculator():
operator=input(('''Welcome to calculator.
DEVELOP BY PRADEEP CHAUREL.
Please select operation which you want.
+ for addition
- for subtraction
* for multiplication
/ for devision
** for power
% for modulo
Enter your choice:'''))

#Take input from user
res=0
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if operator=='+':
    res=num1+num2
    print("Answer:",res)

elif operator=='-':
    res=num1-num2
    print('Answer:',res)

elif operator=='*':
    res=num1*num2
    print('Answer:',res)

elif operator=='/':
    res-num1/num2
    print('Answer:',res)

elif operator=='**':
    res=num1**num2
    print('Answer:',res)

elif operator=='%':
    res=num1%num2
    print('Answer',res)

else:
    print('Invalid operator.')
again()
def again():
cal_again=input('''Do you want to continue this again?
Please type y for YES or n for NO.''')

if cal_again==('y' or 'Y'):
    calculator()
elif cal_again==('n' or 'N'):
    print('''Thanks for using.
    SEE YOU LATER''')
else:
    again()
calculator()

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Max Maizus
#               Kevin Alcantara
#               Rebbeca Eason
#               Miranda Yang
# Section:      578
# Assignment:   4.16 LAB: Pretty equation
# Date:         15 9 2024

a = int(input('Please enter the coefficient A: '))
b = int(input('Please enter the coefficient B: '))
c = int(input('Please enter the coefficient C: '))
_a = ''
_b = ''
_c = ''
#comment
_a_plusMinus = ''
if a==1:
    _a='x^2 '
elif a==-1:
    _a_plusMinus = '- '
    _a='x^2 '
elif a==0:
    _a_plusMinus = ''
elif a<0:
    _a_plusMinus = '- '
    _a= str(-a)+'x^2 '
else:
    _a=str(a)+'x^2 '
_b_plusMinus = '+ '
if b == 1:
    _b = 'x '
elif b == 0:
    _b_plusMinus = ''
elif b == -1:
    _b_plusMinus = '- '
    _b='x '
elif b>0:
    _b= str(b) + 'x '
else:
    _b_plusMinus = '- '
    _b = str(abs(b)) + 'x '
if a==0:
    _b_plusMinus =''
else:
    _b_plusMinus = '' + _b_plusMinus
_c_plusMinus = '+ '
if c == 0:
    #
    if a!=0 and b!=0:
        _c_plusMinus= ''
elif c>0:
    _c= str(c) + ' '
else:
    _c_plusMinus = '- '
    _c = str(-c) + ' '
if a==0 and b==0:
    _c_plusMinus = ' '
else:
    _c_plusMinus = '' + _c_plusMinus
if b==0 and c==0:
    _c_plusMinus = ' '
else:
    _c_plusMinus=''+ _c_plusMinus
if b==0 and c ==0:
    _c_plusMinus = ''
print(f'The quadratic equation is {_a_plusMinus}{_a}{_b_plusMinus}{_b}{_c_plusMinus}{_c}= 0')

#Calculator
def cal(a, b, c):

    if c == '+':
        print(a,' + ', b , ' = ', a + b)

    elif c == '-':
        print(a,' - ', b , ' = ', a - b)

    elif c == '*':
        print(a,' * ', b , ' = ', a * b)
    
    elif c == '/':

        if b != 0:
         print(a,' / ', b , ' = ', a // b)
        else:
            print('0 is not Divisible')


#call
cal(20,4,'/')
    
    

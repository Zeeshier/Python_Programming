def double_it():

    user_input = int(input('Enter a number: '))

    for _ in range(10):
        user_input *= 2  
        print(user_input, end=' ')  

        if user_input >= 100: 
         break

double_it()

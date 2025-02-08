import random 

random_number = random.randint(1,100)
allowed_attempt : int = 5
attempt = 0

print('Welcome to the Guess My Number Game!')
print('I am thinking of a number between 1 and 100.')
print('You have 5 attempts to guess the number.')

while True:
    print(f'You have {allowed_attempt - attempt} attempts left.')

    if attempt == allowed_attempt:
        print('You have run out of attempts. The number was {random_number}')
        break

    user_guess = int(input('Enter your guess: '))
    attempt += 1

    if user_guess < random_number:
        print('Higher')
    elif user_guess > random_number:
        print('Lower')
    else:
        print(f'Congratulations! You guessed the number in {attempt} attempts.')
        break
print('Game Over!')


    
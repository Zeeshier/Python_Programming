import random

prompt : str = 'what do you want? '
jokes: list = [
    "Why don’t skeletons fight each other? Because they don’t have the guts!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the computer go to therapy? It had too many tabs open!",
    "What do you call a fish that wears a bowtie? Sofishticated!",
    "Why don’t eggs tell jokes? Because they might crack up!"
]


def joke_bot():
    user_input = input(prompt)
    
    if user_input.lower() == 'joke':
     print(random.choice(jokes))
    else:
        print('I am a joke bot, I only tell jokes')

joke_bot()

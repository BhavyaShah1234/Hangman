import random

words = ['look', 'fare', 'play', 'fade', 'curl', 'hole', 'zero', 'soil', 'root', 'plan', 'heel', 'food', 'rice',
         'kneel', 'mouse', 'piece', 'graze', 'truck', 'flash', 'style', 'doubt', 'check', 'essay', 'demon', 'lemon',
         'drive', 'dance', 'raid', 'quilt', 'winter', 'wreck', 'wonder', 'zebra', 'lost', 'goat', 'heist', 'icicle',
         'thesis', 'manage', 'deputy', 'direct', 'record', 'ignore', 'design', 'member', 'delete', 'mirror', 'waffle']
word = random.choice(words)
letters = []
for i in word:
    letters.append(i)
name = input('Enter name:')
tries = 10
print(f'The hangman is {name}.\nGuess the word in {tries} tries to save {name}\n-----------------------------')
user = []
for i in range(len(word)):
    user.append('_')
while tries > 0 or user != letters:
    print(f'You have {tries} tries')
    for i in user:
        print(i, end=' ')
    guess = input('\nYour guess:').lower()
    if guess not in letters:
        tries = tries - 1
        if tries == 0:
            print("\n--------------------------------\n        ____\n      O__|\n     /|\\\n     /'\\")
            print(f'{name} is dead.\nYou lose')
            break
    else:
        for index in range(len(letters)):
            if letters[index] == guess:
                break
        if user[index] == '_':
            user[index] = guess
        else:
            for j in range(index, len(letters)):
                if letters[j] == guess:
                    user[j] = guess
    if user == letters:
        for i in user:
            print(i, end=' ')
        print("\n---------------------------------\n  \\O/\n   |\n  / \\\n")
        print(f'\n{name} is saved.\nYou win')
        break

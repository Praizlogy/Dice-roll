#import random
import random



while True:
    roll = input('Roll a dice? (y/n): ').upper()
    if roll == 'Y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1}, {die2})')
    elif roll == 'N':
        print('Thanks for playing')
        break
    else:
        print('Invalid Choice')
    
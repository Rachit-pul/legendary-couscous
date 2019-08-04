import random
num=random.randint(0,100)
firstrun=0
print('to guess a number between 0 and 100')
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
guess_list=[0]
while True:
    guess=int(input('enter your guess '))
    if guess == num:
        print('you win')
        break
    if guess >100 or guess<0:
        print('out of bounds')
        continue
    
    guess_list.append(guess)
    if guess in range(num-10,num+11) and firstrun==0:
        print('WARM')
        firstrun +=1
        continue
    elif guess not in range(num-10,num+11) and firstrun==0:
        print('cold')
        firstrun +=1
        continue
    if abs(num-guess) < abs(num-guess_list[-2]):
        print('warmer')
        continue
    else:
        print('colder')
        continue

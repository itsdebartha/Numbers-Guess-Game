def greater_than_25(num):
    if num>25:
        print('Number is greater than 25.')
    elif num<25:
        print('Number is less than 25.')

def mul_of_3(num):
    if num%3==0:
        print('Number is a multiple of 3.')
    else:
        print('Number is not a multiple of 3.')

def mul_of_5(num):
    if num%5==0:
        print('Number is a multiple of 5.')
    else:
        print('Number is not a multiple of 5.')

def greater_or_less(num1,num2):
    if num1>num2:
        print('Number is greater than your guess')
    elif num1<num2:
        print('Number is less than your guess.')

def is_fact_of_75(num):
    if 75%num==0:
        print('Number is a factor of 75.')
    else:
        print('Number is not a factor of 75.')

print('Guess the number game:\nRules:')
print('The computer has guessed a number between 1 and 50. Your aim will be to guess that number. You have 4 tries in all.')
print('If you guess the number correctly on the first go, you\'ll be awarded 100 points. Else, you\'ll be given one hint. If you guess it then, you\'ll be awarded with 75 points. Else again, you\'ll be given a hint and your point will be 50 if you guess it then. Further if you fail, you\'ll be given a hint again and will be awarded with 25 points.')
print('Still if you fail to guess that number, 0 points will be awarded to you.')
permit=input('Are you ready to start? ')
if permit.lower()=='y' or permit.lower()=='yes' or permit.lower()=='sure' or permit.lower()=='yep' or permit.lower()=='ok' or permit.lower()=='yeah':
    import random
    guess=random.randint(1,50)
    point=0
    i=1
    rand=random.sample(range(1,6),3)
    while i<=4:
        tries=input('Enter your guess: ')
        if tries.isnumeric()==False:
            while tries.isnumeric()==False:
                tries=input('Please enter a valid number between 1 and 50: ')
        if int(tries)==guess:
            if i==1:
                print(f'Congrats!!! You guessed the correct number in only {i} chance...')
            else:
                print(f'Congrats!!! You guessed the correct number in {i} chances...')
            break
        elif i==4:
            print('Sorry buddy!!! You\'ve no chances left.')
            i=0
            break
        else:
            print('Sorry buddy...Here\'s a hint:')
            if rand[i-1]==1:
                greater_than_25(guess)
            elif rand[i-1]==2:
                mul_of_3(guess)
            elif rand[i-1]==3:
                mul_of_5(guess)
            elif rand[i-1]==4:
                greater_or_less(guess,int(tries))
            elif rand[i-1]==5:
                is_fact_of_75(guess)
        i+=1
    if i==1:
        point=100
    elif i==2:
        point=75
    elif i==3:
        point=50
    elif i==4:
        point=25
    else:
        point=0
    print(f'Your point is {point}.\nThe number given by the computer is: {guess}.\nThanks for playing the game.\nGOOD BYE!!!')
else:
    print('Ok!! No problem...')

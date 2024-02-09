import time

print('=============================')
print('        - VictorS -         ')
print(' Calculator made with Python ')
print('        09/02/2024          ')
print('============================= \n')

name = input(f'Enter your name: ')
print(f'\nHello {name} ^_^ !')
while True:
    print('\n1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. About\n')

    numOPER = int(input('Enter the number > '))
    if numOPER == 1:
        print('\nWill you be using fractional numbers?')
        print('1. Yes')
        print('2. No')
        numFRAC = int(input('Enther the number > '))
        if numFRAC == 1:
            numMA = float(input('Enter the largest number > '))
            numME = float(input('Enter the smallest number > '))
            somaAD = numMA + numME
            print(f'\nThe result between {numMA} and {numME} is {somaAD}\n')
            print('Return to the main menu?')
            print('1. Yes')
            print('2. No')
            mainMENU = int(input('Enter the number > '))
            if mainMENU != 1:
                break
                pass
        elif numFRAC == 2:
                numMA = int(input('Enter the largest number > '))
                numME = int(input('Enter the smallest number > '))
                somaAD = numMA + numME
                print(f'\nThe result between {numMA} and {numME} is {somaAD}\n')
                print('Return to the main menu?')
                print('1. Yes')
                print('2. No')
                mainMENU = int(input('Enter the number > '))
                if mainMENU != 1:
                    break
                    pass
    elif numOPER == 2:
        if numOPER == 2:
            print('\nWill you be using fractional numbers?')
            print('1. Yes')
            print('2. No')
            numFRAC = int(input('Enther the number > '))
            if numFRAC == 1:
                numMA = float(input('Enter the minuend > '))
                numME = float(input('Enter the subtrahend > '))
                somaAD = numMA - numME
                print(f'\nThe result of subtracting {numMA} from {numME} is {somaAD}\n')
                print('Return to the main menu?')
                print('1. Yes')
                print('2. No')
                mainMENU = int(input('Enter the number > '))
                if mainMENU != 1:
                    break
                    pass
            elif numFRAC == 2:
                    numMA = int(input('Enter the minuend > '))
                    numME = int(input('Enter the subtrahend > '))
                    somaAD = numMA - numME
                    print(f'\nThe result of subtracting {numMA} from {numME} is {somaAD}\n')
                    print('Return to the main menu?')
                    print('1. Yes')
                    print('2. No')
                    mainMENU = int(input('Enter the number > '))
                    if mainMENU != 1:
                        break
                        pass
    elif numOPER == 3:
        if numOPER == 3:
            print('\nWill you be using fractional numbers?')
            print('1. Yes')
            print('2. No')
            numFRAC = int(input('Enther the number > '))
            if numFRAC == 1:
                numMA = float(input('Enter the first factor > '))
                numME = float(input('Enter the second factor > '))
                somaAD = numMA * numME
                print(f'\nThe result of multiplying {numMA} by {numME} is {somaAD}\n')
                print('Return to the main menu?')
                print('1. Yes')
                print('2. No')
                mainMENU = int(input('Enter the number > '))
                if mainMENU != 1:
                    break
                    pass
            elif numFRAC == 2:
                numMA = int(input('Enter the first factor > '))
                numME = int(input('Enter the second factor > '))
                somaAD = numMA * numME
                print(f'\nThe result of multiplying {numMA} by {numME} is {somaAD}\n')
                print('Return to the main menu?')
                print('1. Yes')
                print('2. No')
                mainMENU = int(input('Enter the number > '))
                if mainMENU != 1:
                    break
                    pass
    elif numOPER == 4:
        if numOPER == 4:
            print('\nWill you be using fractional numbers?')
            print('1. Yes')
            print('2. No')
            numFRAC = int(input('Enther the number > '))
            if numFRAC == 1:
                numMA = float(input('Enter the dividend > '))
                numME = float(input('Enter the divisor > '))
                somaAD = numMA / numME
                print(f'\nThe quotient of dividing {numMA} by {numME} approximately {somaAD}\n')
                print('Return to the main menu?')
                print('1. Yes')
                print('2. No')
                mainMENU = int(input('Enter the number > '))
                if mainMENU != 1:
                    break
                    pass
            elif numFRAC == 2:
                numMA = int(input('Enter the dividend > '))
                numME = int(input('Enter the divisor > '))
                somaAD = numMA / numME
                print(f'\nThe quotient of dividing {numMA} by {numME} approximately {somaAD}\n')
                print('Return to the main menu?')
                print('1. Yes')
                print('2. No')
                mainMENU = int(input('Enter the number > '))
                if mainMENU != 1:
                    break
                    pass
    elif numOPER == 5:
        print('''\nThis was the first 'project' I created using Python. It's my first time learning a programming 
        language, so I definitely didn't use the best structure to build this calculator, but it's working, 
        and that's what matters :)''')
        time.sleep(5)
    else:
        print('\nInvalid input!')

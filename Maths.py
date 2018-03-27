#Possible Additions: store users name for messages, Keep track of how many questions they got right? 

def correctAnswer(prompt, desiredtotal):
    while True:
        try:
            val = int(input(prompt))

        except ValueError:
            print('You have to enter a number! ')
            continue

        if val != int(desiredtotal):
            print('Almost!, try again ')
            continue
        else:
            print('Good job!')
            break
        return val
    
import random
counter = 1 #for use in loops in program
print('Welcome to Maths Quiz! \nA small program for improving your maths skills!')
uname = input('What is your name? \n')




while True:
    print('[A]ddition ')
    print('[S]ubtraction ')
    print('[M]ultiplication ')
    print('[Q]uit ')
    print('Please select an option from the list', uname + '!')
    option = str.lower(input('')) #lowers input so upper and lowercase input is accepted

    if option == 'a':
        print('You selected addition',uname + '!')
        for num in enumerate (range(0,10)):

            addNum1 = random.randint(1,50)
            addNum2 = random.randint(1,50)
            print('Question',counter, '', '','', addNum1, '+', addNum2) #Prints question in correct format with counter
            total = (addNum1 + addNum2)
            
            correctAnswer('Enter your answer: ', total)  #Variable for storing users answer
            counter = counter + 1

    elif option == 's':
        print('You selected subtraction',uname + '!')

        for num in enumerate(range(0,10)):
            subNum1 = random.randint(1,50)
            subNum2 = random.randint(1,50)

            if subNum1 < subNum2:    #Ensures that answer wont be negative by rearranging numbers
                subNum1, subNum2 = subNum2, subNum1

            print('Question',counter, '', '','', subNum1, '-', subNum2)
            subTotal = (subNum1 - subNum2)
            correctAnswer('Enter your answer: ', subTotal) # Function call to reprompt until answer is correct
            counter = counter + 1

    elif option == 'm':
        print('You selected multiplication',uname + '!')

        for num in enumerate(range(0,10)):
            mulNum1 = random.randint(0,10)
            mulNum2 = random.randint(0,10)

            print('Question', counter, '', '', '', mulNum1, 'x', mulNum2)
            mulTotal = (mulNum1 * mulNum2)
            correctAnswer('Enter your answer: ', mulTotal) #Function call uses total variables to compare
            counter = counter + 1

    elif option == 'q':
        print('\nThanks for playing!\nWe hope you enjoyed Maths Quiz!')
        break

    else:
        print('Whoops!, please select one of the options \n')





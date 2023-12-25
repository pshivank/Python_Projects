import random 

c_n = random.randint(1,99)          # this will generate a random between 1 to 99 and store it in variable c_n - computer no. 

print("-------      You have 5 turns to get no.        ------- ")


for s in range(5):                                # running loop for giving 5 turns to user                   
    u_n  =  int(input("Enter Your no. : -- "))    # taking users input and storing it in variable u_n 

    # Now providing hints to user to guess the correct no. 

    if c_n == u_n :
        print('''Congrats ! You Have guessed the no.
                The no. is : -- ''' , c_n)
        
    elif c_n > u_n :
        print("Your guess is too low  , try again ! ...")

    else:
        print("Your guess is too high  , try again ! ...")

print("Game Over ! Play again ...")
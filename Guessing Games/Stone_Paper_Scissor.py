import random 

tasks = ['Stone' , 'Paper' , 'Scissor']       # assigning all tasks 

print(" -------    There Is Five Rounds In This Game      --------")
print(''' Instructions 
          Stone   wins  from   Scissor 
          Scissor  wins from   Paper 
          Paper    wins from   Stone 
          There is 2 winning points and for draw 1 points to each 
      
      ''')


c_p = 0                                                     # taking two variables for storing scores 
u_p = 0 

for s in range(5):
    c_c = random.choice(tasks)                                # from here taking computer's choice 
    u_c   =  input("Enter Your Choice : -- ")                 # taking users choice and storing it in varable u_c

    if c_c == u_c :
        print(" Match Draw !  ...")
        print(" Computer's choice is : -- " , c_c )
        c_p += 1
        u_p += 1

    elif (c_c == 'Stone' and u_c != 'Paper') or (c_c == 'Paper' and u_c != 'Scissor') or ( c_c == 'Scissor' and u_c != 'Stone'):
        print("Computer Wins This Time ! ")
        print(" Computer's choice is : -- " , c_c )
        c_p += 2

    else:
        print("You Win This Time ! .... ")
        print(" Computer's choice is : -- " , c_c )
        u_p += 2


print(  " ------------     Game  Result     ---------------- ")


if c_p == u_p :
    print("Match draw ! .... ")
    print("your point : -- " , c_p )
    print(" Computer's point :-- " , u_p)

elif c_p > u_p :
    print("Sorry You Loose ! ....")
    print("your point : -- " , u_p )
    print(" Computer's point :-- " , c_p)

else:
    print("Congratulations ! You won the game...")
    print("your point : -- " , u_p )
    print(" Computer's point :-- " , c_p)



import random
rounds = 0
points_p1 = 0
points_p2 = 0
intro = 0

x = 'not'
y = 'and'
z = 'or'
a = 'xor'


while intro != 1:
    print("Hello! As a programmer, it's important to evaluate logical operators with respect to precedence.")
    print("It's similar to math class where you learn the order of operations or PEMDAS."+'\n')
    print("Let's learn precedence through the game rock, paper, scissors!"+'\n')

    print("Key:"+'\n')
    print("not > and")
    print("not > or")
    print("not > XOR")
    print("or == XOR")
    print("and > or"+'\n')
    
    print("Rules: Study the key for as long as you need and enter the word 'ready' to begin the game.")
    print("There will be 10 rounds, the objective isn't to win but understand which counters which.")
    answer = input("Begin the game?: ")
    print('\n')

    if answer == 'ready':
        intro = 1
        while rounds < 11:
            p1 = input("Enter one of the following (and,or,xor,not): ")
        
            computer = random.randint(1,4)
            if computer == 1:
                p2 = a
            elif computer == 2:
                p2 = x
            elif computer == 3:
                p2 = y
            elif computer == 4:
                p2 = z
            
            print("You:",p1,"Computer:",p2)
        
            if p1 == p2:    #tie method
                print("It's a tie")     
                rounds+=1
            elif (p1 == 'or' and p2 == a) or (p1 == 'xor' and p2 == z):
                print("It's a tie")
                rounds+=1
            
            elif (p1 == 'or' and p2 == y) or (p1 == 'or' and p2 == x):  #or method
                print("Computer wins this round.")
                points_p2+=1
                rounds+=1
            elif (p1 == 'and' and p2 == z) or (p1 == 'not' and p2 == z):
                print("You win this round!")
                points_p1+=1
                rounds+=1

            elif (p1 == 'and' and p2 == x): #and method
                print("Computer wins this round.")
                points_p2+=1
                rounds+=1
            elif (p1 == 'not' and p2 == y):
                print("You win this round!")
                points_p1+=1
                rounds+=1

            elif (p1 == 'xor' and p2 == x): #adding missing methods #1
                print("Computer wins this round.")
                points_p2+=1
                rounds+=1
            elif (p1 == 'not' and p2 == a):
                print("You won this round!")
                points_p1+=1
                rounds+=1

            elif (p1 == 'xor' and p2 == y): #adding missing methods #2
                print("Computer wins this round.")
                points_p2+=1
                rounds+=1

            elif (p1 == 'and' and p2 == a):
                print("You won this round!")
                points_p1+=1
                rounds+=1

            if rounds == 10:
                if points_p1 > points_p2:
                    print("Congratulations, you win the game :)!")
                    rounds = 11
                elif points_p1 < points_p2:
                    print("Better luck next time, Computer won the game.")
                    rounds = 11
                elif points_p1 == points_p2:
                    print("Looks like it's a tie. Let's play again sometime!")
                    rounds = 11
                
        

    

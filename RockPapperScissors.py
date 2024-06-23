import random
print("WELCOME TO ROCK PAPPER SCISSORS GAME")
list=['r','p','s']
def game(list):
    your_score=0
    computer_score=0
    tie_matches=0
    for i in range(0,5):
        computer_choice=random.choice(list)
        user_choice=input("Enter your choice(r/p/s):")
        if (computer_choice=='r'):
            if (user_choice=='p'):
                print("You won ")
                your_score+=1
            elif (user_choice=='s'):
                print("computer won ")
                computer_score+=1
            elif (user_choice=='r'):
                print("Tie match")
                tie_matches+=1
        elif (computer_choice=='p'):
            if (user_choice=='s'):
                print("You won")
                your_score+=1
            elif (user_choice=='r'):
                print("Computer won ") 
                computer_score+=1
            elif (user_choice=='p'):
                print("Tie match ")
                tie_matches+=1
        elif (computer_choice=='s'):
            if (user_choice=='r'):
                print("You won ")
                your_score+=1
            elif (user_choice=='p'):
                print("Computer won ")
                computer_score+=1
            elif (user_choice=='s'):
                print("Tie match") 
                tie_matches+=1
        print("computer's choice:",computer_choice)
    print("YOUR SCORE=",your_score,"\t","COMPUTER SCORE=",computer_score,"\t","NO.OF TIES=",tie_matches)
    if your_score>=computer_score:
        print("---AWESOME!YOU WON THE MATCH---")
    else:
        print("---COMPUTER WON THE MATCH---")
game(list)
while True:
    m=input("Do you want to play again:(yes/no):")
    if m=='yes':
        game(list)
    else:
        print("Thank you :)")
        break


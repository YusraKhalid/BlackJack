import random

def main():
    dealerCArd1 = random.randint(2,11) #taking to cardds for dealer and two for player.
    dealerCArd2 = random.randint(2,11)
    playerCArd1 = random.randint(2,11)
    playerCArd2 = random.randint(2,11)

    flag = True
    rerun = True #it is used for not asking to hit agin and again after first time user does not hit..
    print("Your two cards are: ",playerCArd1,playerCArd2)
    print("Delears one card is: ",dealerCArd1)

    dealerTotal = dealerCArd1 + dealerCArd2
    playerTotal = playerCArd1 + playerCArd2
    dealerDisplayableTotal = dealerCArd1 #as one card is hidden
    print("Your total is: ", playerTotal)
    #The player can hit maximum 11 times, as if he gets the minimum card everytime (i.e. 2) he will be busted at 11th hit. So range is 11.
    for var in range(11): #if anyone gets busted. the game(loop) ends.
        if (playerTotal > 21) and (flag == True):
            print("""***Busted***
            You lose""")
            flag = False
            break

        elif (dealerTotal > 21) and (flag == True):
            print("You win!!! Dealer got busted.")
            flag = False
            break
        if flag == True and rerun == True:
            hit = input("Do you want to hit(Y/N)?")
            if hit == "Y" or hit == "y":
                newCardPlayer = random.randint(2,11)
                print("New card is: ", newCardPlayer)
                playerTotal += newCardPlayer
                print("Your Total is: ",playerTotal)
            elif (hit == "N") or (hit == "n"):
                rerun = False
        if dealerTotal < 16: #delear draw card is the toal is less than 16
            dealerNewCard = random.randint(2,11)
            dealerDisplayableTotal += dealerNewCard
            dealerTotal += dealerNewCard
            print("Dealer new card is: ",dealerNewCard)
            print("Total of dealer with one hidden card is: ",dealerDisplayableTotal)
    if (flag == True):
        if (playerTotal > dealerTotal):
            print("You win :-D")
            print("Dealer total is: ", dealerTotal)
        elif playerTotal <= dealerTotal:
            print("You lose :-(")
            print("Dealer total is: ",dealerTotal)

main()


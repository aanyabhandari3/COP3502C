from p1_random import P1Random
rng = P1Random()

menu = " 1. Get another card \n 2. Hold hand \n 3. Print statistics \n 4. Exit\n"

game_play = True
counter = 0
player_wins = 0
dealer_wins = 0
tie_wins = 0

while game_play:
# activate counter and game head
    counter += 1
    print("START GAME #", counter, "\n")

#variables for random generation of player card and hand   
    card_value = rng.next_int(13) + 1
    hand = 0

    if card_value<= 10:
        if card_value == 1:
            card = str("ACE")
            hand = 1
        else:
            card = str(card_value)
            hand = card_value
    else:
        if card_value == 11:
            card = str("JACK")
            hand = 10
        elif card_value == 12:
            card = str("QUEEN")
            hand = 10
        else:
            card = str("KING")
            hand = 10

    print("Your card is a " + card +"!")
    print("Your hand is: ", hand, "\n")


#loop for continuing game play based on option
    no_winner = True

    while no_winner:
        print(menu)
        option = int(input("Choose an option: "))

        if option == 1:
            card_value = rng.next_int(13) + 1

            if card_value <= 10:
                if card_value == 1:
                    card = str("ACE")
                    hand += card_value
                    
                else:
                    card = str(card_value)
                    hand += card_value

    
            else:
                if card_value == 11:
                    card = str("JACK")
                    hand += 10

                       
                elif card_value == 12:
                    card = str("QUEEN")
                    hand += 10

                     
                else:
                    card = str("KING")
                    hand += 10

             
            print("\nYour card is a " + card +"!")
            print("Your hand is: ", hand, "\n")

            if hand == 21:
                print("BLACKJACK! You win!\n")
                player_wins += 1
                no_winner = False
            elif hand > 21:
                print("You exceeded 21! You lose.\n")
                dealer_wins += 1
                no_winner = False

            
        elif option == 2:
            dealer = rng.next_int(11) + 16
            
            print("\nDealer's hand: ", dealer)
            print("Your hand is: ", hand, "\n")

            if dealer > 21:
                print("You win!\n")
                player_wins +=1
                no_winner = False

            elif dealer == hand:
                print("It's a tie! No one wins!\n")
                tie_wins += 1
                no_winner = False

            elif dealer < hand:
                print("You win!\n")
                player_wins += 1
                no_winner = False
            
            elif (hand > 21) or (hand < dealer):
                print("Dealer wins!\n")
                dealer_wins += 1
                no_winner = False
                
            else:
                print("no good")
                pass
        elif option == 3:
            counter -= 1

            percent = (player_wins/ counter)*100

            print("\nNumber of Player wins: ", player_wins)
            print("Number of Dealer wins: ", dealer_wins)
            print("Number of tie games: ", tie_wins)
            print("Total # of games played is: ", counter)
            print("Percentage of Player wins: ",percent, "%\n")
    
        elif option == 4:
                no_winner = False
                game_play = False
    
        else:
            counter -= 1
            print("Invalid input! \nPlease enter an integer value between 1 and 4.\n")
    



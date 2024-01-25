import random

class NineFingers: # Class NineFingers this is the game blueprint when class is called this is where the game will actually give outputs 
    def __init__(self):
        self.player_fin = 9 # Starting amount of fingers/lives for both players  
        self.azrael_fin = 9
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 # A deck of cards has 52 cards, 4 of each card value from 1/11 to the 4 face cards all with the value of 10  
        self.player_hand = [] 
        self.azrael_hand = [] #both of the players hands will start empty 
    

    def hit(self): # this method would randomly pick a card from the deck and give the value to either player
        return random.choice(self.deck)

    def open_inv(self): # Planned to have items that would make gameplay much more strategy based for exmaple one item "scissors" would cut one of the cards in the players hand another item "glasses" would reveal one of the Azraels cards etc;
        print("Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}") # End of every round you would get one random item and items couldve been mid round at the start of the game you wouldve been given 3 or 5 random items could have had multuple of one item

    def azrael_sc(self): # This Method calculates the total score of the hand of the Azrael "Azrael"
        score = sum(self.azrael_hand)
        return score

    def player_sc(self): # This Method calculates the total score of the hand of the player
        score = sum(self.player_hand)
        return score

    def dis_fin(self): # This method would show how many lifes/fingers each players has 
        print(f"Your fingers: {self.player_fin}    Azrael's fingers: {self.azrael_fin}\n")

    def start_round(self): # When a new round is started each player must be dealt 2 cards to start this method will do that deal each player 2 cards when called 
        self.player_hand = [self.hit(), self.hit()]
        self.azrael_hand = [self.hit(), self.hit()]

    def play_round(self): # This Method is the game, it is where everything above comes in to play and works with each other to make the gameplay
        print("\nYou have been given two cards")
        self.start_round() # When play_round is called the first thing it must do is deal the 2 players their starting 2 cards 

        # This is where the start of the players turn begins it shows the players hand currently and they total score 
        print(f"\nYour Hand {self.player_hand}, current score: {self.player_sc()}\n")
        print(f"The Azrael Hand {[ '?' for _ in self.azrael_hand]}") #This line is for showing the Azraels hand but because we dont want the player to know what cards Azrael has for every value that is in Azrael hand it will show a ? 

        wdyd = input("\nDo you 'hit' or 'stand' or 'inventory': ").lower() # This is where the Player gets to choose what they would like to do on their turn 

        while True: # this while loop will make it so unless one of the conditions that will break the loop is met it will keep looping the code writien below it making the player either go over 32 or choose stand ending the players turn and round
            if wdyd == 'hit':
                print("==================================================================================")
                self.player_hand.append(self.hit()) # If choosen hit it will call the hit method to pick a random card from the given deck and add it to the player_hand list
                print(f"You pick up a card: {self.player_hand[-1]}") # This will show the card that the player has most recently picked up because -1 in player_hand will always be number at the end of the list 
                if self.player_sc() > 32:
                    print("You went over 32.")
                    break # If the player hits and their total score it more than 32 break the while loop 

                # This is where the Azrael will decide what to do depending on his hands total score but only after the player has choosen hit and if their total score did not exceed 32
                if self.azrael_sc() < 26: 
                    self.azrael_hand.append(self.hit())
                    print("\nThe Azrael has chosen to 'Hit'. He picks up a card") # The program will make Azrael hit if the total calculated score of his hand is under 26 
                    print("==================================================================================")
                elif self.azrael_sc() >= 26: 
                    print("\nThe Azrael has chosen to 'Stand'") # If Azraels hand total score is more than or equal to 26 he is forced to stand 
                    print("==================================================================================")
                if self.azrael_sc() > 32:
                    print("\nThe Azrael went over 32.") # If Azraels hand total score is 32 at any point in the round this will break the while loop  
                    print("==================================================================================")
                    break

                # This code will make it the players turn again after Azrael has made his decidion 
                print(f"Your Hand {self.player_hand}, current score: {self.player_sc()}\n") # Shows your hand and your hands total score
                print(f"The Azrael Hand {[ '?' for _ in self.azrael_hand]}") # Shows Azraels hand 
                wdyd = input("\nDo you 'hit' or 'stand': ").lower() # Will repeat the same options to the player as from the start of the round 
            
            elif wdyd == 'stand': # This elif code is for when the player has choosen to stand 
                print("==================================================================================")
                print("You have chosen to Stand") # Because the Player has choosen stand they will not be given any more options until this round is over 
                if self.azrael_sc() < 26: # Same code from above the program will make Azrael hit or stand depending on his hands total score
                    self.azrael_hand.append(self.hit())
                    print("\nAzrael has chosen to 'Hit'. He picks up a card")
                    print("==================================================================================")
                elif self.azrael_sc() >= 26:
                    print("\nAzrael has chosen to 'Stand'")
                    print("==================================================================================")  #Azrael will keep choosing to hit until his hands total is more than or equal to 26 where he will stand or his hands score goes over 32 where he will lose both will break the while loop 
                    break
                elif self.azrael_sc() > 32:
                    print("\nAzrael went over 32. He has lost a finger")
                    print("==================================================================================")
                    break
            
            elif wdyd == 'inventory':
                self.open_inv()


        print(f"\nYour hand {self.player_hand} You had: {self.player_sc()}") #When the while loop is finished, this is where the results of the round are shown it will show your hand and the total score and the same for Azrael but it also will reveal his hand
        print(f"Azrael's hand {self.azrael_hand} He had: {self.azrael_sc()}\n")

        if self.player_sc() > 32: # if the total score of the hand of the player exceeds 32 they have lost the round and they will lose a finger
                print("You went over 32. You have lost a finger.")
                self.player_fin -= 1 
        elif self.azrael_sc() > 32: # if the total score of the hand of Azrael exceeds 32 they have lost the round and they will lose a finger
                print("The Azrael went over 32. He has lost a finger.")
                self.azrael_fin -= 1
        elif self.player_sc() > self.azrael_sc(): # If the players hands total score is a higher value then Azraels then Azraels will lose a finger and the player will win 
                print("You Won, he cuts one off his finger.\n")
                self.azrael_fin -= 1
        elif self.player_sc() < self.azrael_sc(): # If Azraels hands total score is a higher value then the players then the player will lose a finger and Azrael will win 
                print("You Lost, he takes a finger.\n")
                self.player_fin -= 1
        else:
                print("None of you have won.\n") # This is for when the values of both the players hands are the same leading to a tie 

        self.dis_fin() # Shows the number of fingers remaining on both players 
        print("==================================================================================")


    def play_game(self): # this method determines when to stop the game 
        while self.player_fin > 0 and self.azrael_fin > 0: # if both of players fingers value is more than 0 it will call play_round to start another round again it will keep doing this intill one of the players fingers value hits 0 
            self.play_round()

        if self.player_fin <= 0: # if the players finger value is less than or equal to zero it will print out the given ending, and ending the program 
            print("The restraints snap open")
            print("You lay in shock as you look at 9 of your fingers laying on the cold table, leaving nothing remaining but 1 finger. The man stands up from the table and leaves without saying a word, closing the door behind him. You frantically jump up from the table to follow after, but when you get to the door, you are not able to turn the doorknob. You freeze to death in the cabin.")
        else: # if not the players finger value being less than or equal to zero it means Azraels finger value has hit less than or equal to zero which will print out the given ending writien below and ending the program
            print("The restraints snap open")
            print("You look at the man as 9 of his fingers lay on the table cold. He points at the shelf where the keys to the door lay still. As you get up to fetch them to leave, you can hear the man speaking to himself quietly, 'The lord is my shepherd, for there is nothing I lack, in green pastures he makes me lie down, to still waters h-', you leave the room before you can hear any more.")


print("The smell of chemicals and the feel of a cold wet cloth jolt you awake, you find yourself strapped the chair you just awoke in, the air is cold, and with every breath you take you feel a \nsharp pain in your chest. As you look around you cant see much in the room but the table that sits in front of you. You try to remember where you were before all of this ")
print("What do you remember")
print("\nPriest; Items will prove to be slightly more useful\nThe last thing you can remember is the sound of chruch bells")  # All of this is the dialogue that is given to the player before the main game can begin this is also where the player wouldve been able to choose on their class/ who they play as 
print("\nThief; Whats yours is mine\nThe last thing you remember is running you not entirely sure from what")
print("\nScholar; You majored in Math with an emphasis in probability and statistics\nThe last thing you can remember is walking around on your college campus")

while True:
    role = input("\nWhat do you remember (Priest, Thief, Scholar): ")   # I used a while loop here so the player is forced to decide from the 3 given options of class if input doesnt match one of the options they would be asked again 

    if role == 'Priest':
        print("\nMay the Lord show mercy on us all.")
        break
    elif role == 'Thief':
        print("\nYou remembered you were running from a store owner")
        break                                                            # This code would make the player decide on what class they would like to play as
    elif role == 'Scholar':
        print("\nNerd.")
        break
    else:
        print("Thats not right")
            
print("As you slightly come back to your senses you hear someone walking behind you. As the footsteps get closer you get a \noverwhelming feeling of dread. You see the figure walk by you and sit in the chair directly across the table from you. He opens his mouth and starts speaking to you")
print("You are a sinner, for all have sinned and fall short of the glory of God, and for the wages of sin is death. \nYet the steadfast love and mercy of the Lord never ceases for those who reach out and seek it. He stops talking and looks at you, you feel obligated to respond")
        # Once class selection has been made now there is one more option before the class 9fingers can begin which is for the player to decide if they would like to play the game at all 

while True:
    answer = input("Do you reach out (Yes or No): ")    # Again a while loop is used to force the player to decide on 1 of the 2 given options 

    if answer == "Yes":
        print("The man sits back in his chair and pulls out a deck of cards and a knife from his pockets. He says to you \n'Closest to 32 wins, Over 32 and you will lose'")
        game = NineFingers() # If the player decides yes this code "game = NineFingers()" will make an object from the class NineFingers 
        game.play_game() # And this code will take the object made from the class NineFingers and actually start it by giving the play_game method a parameter 
        break
    elif answer == "No":
        print("The man stands up and leaves the room, closing the door behind him. With your restraints still tying you to the chair, you are helpless to do anything. You freeze to death.")
        break
    else: 
        print("Thats not right")
        
import random

card_suits = ("Clubs", "Diamonds", "Hearts", "Spades")
card_ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")


class Card:

    def __init__(self, suit, rank):  # Method that defines the card attributes, each card has a suit and a rank
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit  # Returns a string of the cards rank and suit ie. Two of Clubs


class Deck:

    def __init__(self):  # Method to create a deck of 52 cards from the above card suits and ranks
        self.deck = []  # Starts as an empty list
        for suit in card_suits:
            for rank in card_ranks:
                self.deck.append(Card(suit, rank))  # Adds one of each card rank to each suit and adds it to the list

    def shuffle(self):
        random.shuffle(self.deck)  # This is a method that shuffles the entries in the list that make up the deck

    def deal_card(self):  # This is a method that deals a card by 'popping' the first entry in the deck
        dealt_card = self.deck.pop()
        return dealt_card


card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
               "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}  # Remember Ace can be 11 or 1


class Hand:

    def __init__(self):
        self.cards = []  # Both players start with an empty hand
        self.value = 0  # Both players hands start with a total value of 0
        self.aces = 0  # Both players hands start without any aces

    def add_card_to_hand(self, card):  # This is a method to add cards to a hand
        self.cards.append(card)  # This adds a card to a hand
        self.value = self.value + card_values[card.rank]  # This updates the value of a hand
        if card.rank == "Ace":  # This tracks the number of aces in a hand so the ace value can be changed from 11 to 1
            self.aces = self.aces + 1

    def adjust_value_of_ace(self):  # This changes the value of an ace if needed
        while self.value > 21 and self.aces >= 1:
            self.value = self.value - 10
            self.aces = self.aces - 1


def hit_me(deck, hand):  # This functions adds a card to a hand, as well as updating the value of aces when called
    hand.add_card_to_hand(deck.deal_card())
    hand.adjust_value_of_ace()


def show_initial_hand(player, player_name, dealer):  # This function shows the initial hand - 1 dealer card and both
    # player cards
    print("\nThe Dealer's Hand:")
    print("Hidden_Card")
    print(dealer.cards[1])
    print("\n{}'s Hand:".format(player_name))
    print(*player.cards, sep="\n")
    print("\nThe total value of your hand is:", player.value)


def show_players_hand(player, player_name):  # This function shows only the players hand
    print("\n{}'s Hand:".format(player_name))
    print(*player.cards, sep="\n")
    print("\nThe total value of your hand is:", player.value)


def show_dealers_hand(dealer):  # This function shows only the dealers hand
    print("\nThe Dealer's Hand:", *dealer.cards, sep="\n")
    print("\nThe total value of the Dealer's hand is:", dealer.value)


def show_all_cards(player, player_name, dealer):  # This function shows all cards in play
    print("\nThe Dealer's Hand:", *dealer.cards, sep="\n")
    print("\nThe total value of the Dealer's hand is:", dealer.value)
    print("\n{}'s Hand:".format(player_name), *player.cards, sep="\n")
    print("\nThe total value of your hand is:", player.value)


def place_bet(player_chips):  # This function governs player betting
    player_bet = 0
    print("\nYou currently have {} chips".format(player_chips))
    player_chips = int(player_chips)
    while not player_bet or not isinstance(player_bet, int):
        try:
            player_bet = int(input("\nPlease enter your bet: "))
        except ValueError:
            print("\nPlease enter a valid integer!")
        else:
            break

    if player_bet <= 0:
        print("\nPlease enter a valid bet!")

    if player_bet > player_chips:
        print("\nYou do not have that many chips, please enter a valid bet!")

    else:
        return player_bet


def play_again(number_of_games, player_name, player_score, dealer_score, player_chips, gambling, total_bet_value,
               total_winnings, total_losses):
    # This function allows the player to play again, keeping all the stats from the previous session
    print("\n-------------------------------------------------------------------------------------------------")
    continue_playing = input("\nWould you like to play again? (Y/N): ")

    while not continue_playing or continue_playing[0].upper() != "Y" and continue_playing[0].upper() != "N":
        print("Please enter a valid input {}!".format(player_name))
        continue_playing = input("\nWould you like to play again? (Y/N): ")

    if continue_playing.lower()[0] == "y":
        game_play(number_of_games + 1, player_name, player_score, dealer_score, player_chips, gambling, total_bet_value,
                  total_winnings, total_losses)

    else:
        number_of_games = number_of_games + 1
        print("\n-------------------------------------------------------------------------------------------------")
        print("\n{} played".format(player_name), number_of_games, "game(s). {} won".format(player_name), player_score,
              "game(s) and lost", dealer_score, "game(s) for a final win ratio of:",
              int((player_score / number_of_games) * 100), "%")
        if gambling[0].upper() == "Y":
            print("\n{0} bet {1} chips. {0} won {2} chips and lost {3} chips ".format(player_name, total_bet_value,
                                                                                      total_winnings, total_losses))
        print("\n-------------------------------------------------------------------------------------------------")
        exit(0)


def game_play(number_of_games, player_name, player_score, dealer_score, player_chips, gambling, total_bet_value,
              total_winnings, total_losses):
    # This is the main function that governs how the game is played
    play_game = True
    instances_of_program_run = number_of_games

    if instances_of_program_run < 1:

        player_name = input("\nPlease enter your name: ")

        while not player_name:
            print("Please enter a valid input!")
            player_name = input("\nPlease enter your name: ")

        player_name = player_name.upper()[0] + player_name.lower()[1:]

        first_time = input("\nHello {}, is this your first time playing Blackjack? (Y/N): (Please enter Y if this is "
                           "your first time running this program)".format(player_name))

        while not first_time or first_time[0].upper() != "Y" and first_time[0].upper() != "N":
            print("Please enter a valid input {}!".format(player_name))
            first_time = input("\nHello {}, is this your first time playing Blackjack? (Y/N): (Please enter Y if this "
                               "is your first time running this program)".format(player_name))

        if first_time.lower()[0] == "y":
            print(
                "\nWelcome to Blackjack (21), In this game your objective is to get a score as close to 21 as "
                "possible. "
                "\nYou will win if you are closer to 21 than the Dealer. \nIf you go above 21 you will go bust and the "
                "Dealer will win. "
                "\nAt the start of the game, both you and the Dealer will be dealt 2 cards, "
                "you will then be asked to 'Hit' (take another card) or 'Stand' (keep your current hand). "
                "\nOnce you 'Stand' the Dealer will then 'Hit' or 'Stand' and the player whose cards has value "
                "closest to 21 will win the game.")

        start_the_game = str(input("\n{}, Are you ready to play Blackjack? (Y/N): ".format(player_name)))

        while not start_the_game or start_the_game[0].upper() != "Y" and start_the_game[0].upper() != "N":
            print("Please enter a valid input {}!".format(player_name))
            start_the_game = str(input("\n{}, Are you ready to play Blackjack? (Y/N): ".format(player_name)))

        if start_the_game.lower()[0] == "y":
            print("Ok, then lets start the game!")

        else:
            are_you_sure = input("Are you sure you want to exit the game? (Y/N): ")
            while not are_you_sure or are_you_sure[0].upper() != "Y" and are_you_sure[0].upper() != "N":
                print("Please enter a valid input {}!".format(player_name))
                are_you_sure = input("Are you sure you want to exit the game? (Y/N): ")

            if are_you_sure.upper()[0] == "Y":
                exit(0)

            else:
                print("Ok, then lets start the game!")

        print("\n-------------------------------------------------------------------------------------------------")

        print("\nAs this is your first game, the house has kindly offered to start you off with 500 chips!")

        gambling = input("Would you like to play with chips? (Y/N): ")
        if not gambling or gambling[0].upper() != "Y" and gambling[0].upper() != "N":
            print("Please enter a valid input {}!".format(player_name))
            gambling = input("Would you like to play with chips? (Y/N): ")

        total_bet_value = 0
        total_winnings = 0
        total_losses = 0

        print("\n-------------------------------------------------------------------------------------------------")

    elif instances_of_program_run >= 1:

        same_name = input("Is that still you {}? (Y/N): ".format(player_name))

        while not same_name or same_name[0].upper() != "Y" and same_name[0].upper() != "N":
            print("Please enter a valid input {}!".format(player_name))
            same_name = input("Is that still you {}? (Y/N): ".format(player_name))

        if same_name.lower()[0] == "y":
            print("\n-------------------------------------------------------------------------------------------------")
            print("\nYou have played", number_of_games, "game(s) {}".format(player_name))
            print("Your score is", player_score, "\nThe Dealer's score is", dealer_score)
            if gambling[0].upper() == "Y":
                print("\nYou have bet {0} chips. You have won {1} chips and lost {2} chips ".format(total_bet_value,
                                                                                                    total_winnings,
                                                                                                    total_losses))

            if player_chips == 0:
                print("\nUnfortunately you have run out of chips and have been asked to leave")

                carry_on = input("{} Do you really want to play again? (Y/N): ".format(player_name))

                while not carry_on or carry_on[0].upper() != "Y" and carry_on[0].upper() != "N":
                    print("Please enter a valid input {}!".format(player_name))
                    carry_on = input("{} Do you really want to play again? (Y/N): ".format(player_name))

                if carry_on[0].upper() == "Y":
                    player_chips = 100
                    print("\nA nearby wealthy patron takes pity on you and gives you 100 chips")

                else:
                    exit(0)

            print("\n-------------------------------------------------------------------------------------------------")

        else:
            print("\n-------------------------------------------------------------------------------------------------")
            print("{} played".format(player_name), number_of_games, "game(s). {} won".format(player_name), player_score,
                  "game(s) and lost", dealer_score, "game(s) for a final win ratio of:",
                  int((player_score / number_of_games) * 100), "%")
            if gambling[0].upper() == "Y":
                print("\n{0} bet {1} chips. {0} won {2} chips and lost {3} chips ".format(player_name,
                                                                                          total_bet_value,
                                                                                          total_winnings,
                                                                                          total_losses))
            print("\n-------------------------------------------------------------------------------------------------")

            player_score = 0
            dealer_score = 0
            number_of_games = 0
            player_chips = 500

            player_name = input("\nPlease enter your name: ")

            while not player_name:
                print("Please enter a valid input!")
                player_name = input("\nPlease enter your name: ")

            player_name = player_name.upper()[0] + player_name.lower()[1:]

            first_time = input(
                "\nHello {}, is this your first time playing Blackjack? (Y/N): (Please enter Y if this is "
                "your first time running this program)".format(player_name))

            while not first_time or first_time[0].upper() != "Y" and first_time[0].upper() != "N":
                print("Please enter a valid input {}!".format(player_name))
                first_time = input(
                    "\nHello {}, is this your first time playing Blackjack? (Y/N): (Please enter Y if this "
                    "is your first time running this program)".format(player_name))

            if first_time.lower()[0] == "y":
                print(
                    "\nWelcome to Blackjack (21), In this game your objective is to get a score as close to 21 as "
                    "possible. "
                    "\nYou will win if you are closer to 21 than the Dealer. \nIf you go above 21 you will go bust "
                    "and the Dealer will win. "
                    "\nAt the start of the game, both you and the Dealer will be dealt 2 cards, "
                    "you will then be asked to 'Hit' (take another card) or 'Stand' (keep your current hand). "
                    "\nOnce you 'Stand' the Dealer will then 'Hit' or 'Stand' and the player whose cards has value "
                    "closest to 21 will win the game.")

            start_the_game = str(input("\n{}, Are you ready to play Blackjack? (Y/N): ".format(player_name)))

            while not start_the_game or start_the_game[0].upper() != "Y" and start_the_game[0].upper() != "N":
                print("Please enter a valid input {}!".format(player_name))
                start_the_game = str(input("\n{}, Are you ready to play Blackjack? (Y/N): ".format(player_name)))

            if start_the_game.upper()[0] == "Y":
                print("Ok, then lets start the game!")

            else:
                are_you_sure = input("Are you sure you want to exit the game? (Y/N): ")
                while not are_you_sure or are_you_sure[0].upper() != "Y" and are_you_sure[0].upper() != "N":
                    print("Please enter a valid input {}!".format(player_name))
                    are_you_sure = input("Are you sure you want to exit the game? (Y/N): ")

                if are_you_sure.upper()[0] == "Y":
                    exit(0)

                else:
                    play_game = True
                    print("Ok, then lets start the game!")

            print("\nAs this is your first game, the house has kindly offered to start you off with 500 chips!")

            gambling = input("Would you like to play with chips? (Y/N): ")
            if not gambling or gambling[0].upper() != "Y" and gambling[0].upper() != "N":
                print("Please enter a valid input {}!".format(player_name))
                gambling = input("Would you like to play with chips? (Y/N): ")

            total_bet_value = 0
            total_winnings = 0
            total_losses = 0

    bet = 0

    if gambling[0].upper() == "Y":
        bet = place_bet(player_chips)
        if not isinstance(bet, int):
            bet = place_bet(player_chips)
        player_chips = player_chips - bet

    print("\n-------------------------------------------------------------------------------------------------")

    deck = Deck()
    print("\nThe Deck will now be shuffled and cards dealt!")
    deck.shuffle()

    dealer_hand = Hand()
    dealer_hand.add_card_to_hand(deck.deal_card())
    dealer_hand.add_card_to_hand(deck.deal_card())

    player_hand = Hand()
    player_hand.add_card_to_hand(deck.deal_card())
    player_hand.add_card_to_hand(deck.deal_card())

    player_hand.adjust_value_of_ace()  # In case of the 0.00443786982 chance of the player being dealt two Aces in
    # their initial hand - this happened during my testing!
    show_initial_hand(player_hand, player_name, dealer_hand)

    while play_game:

        h_or_s = input("\n{} Would you like to 'Hit' or 'Stand'? (H/S): ".format(player_name))

        while not h_or_s or h_or_s[0].upper() != "S" and h_or_s[0].upper() != "H":
            print("Please enter a valid input {}!".format(player_name))
            h_or_s = input("\n{} Would you like to 'Hit' or 'Stand'? (H/S): ".format(player_name))

        if h_or_s[0].upper() == "H":
            hit_me(deck, player_hand)

        elif h_or_s[0].upper() == "S":
            print("\nThe dealer will now play.")
            play_game = False

        show_players_hand(player_hand, player_name)

        if player_hand.value > 21:
            print("You have gone bust. The Dealer wins!")
            dealer_score = dealer_score + 1
            if gambling[0].upper() == "Y":
                total_bet_value = total_bet_value + bet
                total_losses = total_losses + bet
            break

    if player_hand.value <= 21:

        show_dealers_hand(dealer_hand)
        print("\nThe Dealer will now choose to hit until the value of their deck is equal to 17 or higher")

        while dealer_hand.value < 17:
            hit_me(deck, dealer_hand)

        show_all_cards(player_hand, player_name, dealer_hand)

        if dealer_hand.value > 21:
            if player_hand.value == 21:
                print("\nCongratulations {} you have won this game and its a Blackjack!".format(player_name))
                player_score = player_score + 1
                if gambling[0].upper() == "Y":
                    total_bet_value = total_bet_value + bet
                    total_winnings = int(total_winnings + (bet * 1.5))
                    player_chips = int(player_chips + bet + (bet * 1.5))
                    print("You bet {} chips and won with a Blackjack, so now you have {} chips!".format(bet,
                                                                                                        player_chips))

            else:
                print("\nCongratulations {} you have won this game!".format(player_name))
                player_score = player_score + 1
                if gambling[0].upper() == "Y":
                    total_bet_value = total_bet_value + bet
                    total_winnings = total_winnings + bet
                    player_chips = player_chips + (bet * 2)
                    print("You bet {} chips and won, so now you have {} chips!".format(bet, player_chips))

        elif dealer_hand.value == player_hand.value:
            print("\nUnlucky {}, its a draw so the Dealer wins!".format(player_name))
            dealer_score = dealer_score + 1
            if gambling[0].upper() == "Y":
                player_chips = player_chips + bet
                print("You bet {} chips and drew so your bet is returned, you now have {} chips!".format(bet,
                                                                                                         player_chips))

        elif dealer_hand.value > player_hand.value:
            print("\nThe Dealer wins!")
            dealer_score = dealer_score + 1
            if gambling[0].upper() == "Y":
                total_bet_value = total_bet_value + bet
                total_losses = total_losses + bet

        elif dealer_hand.value < player_hand.value:
            if player_hand.value == 21:
                print("\nCongratulations {} you have won this game and its a Blackjack!".format(player_name))
                player_score = player_score + 1
                if gambling[0].upper() == "Y":
                    total_bet_value = total_bet_value + bet
                    total_winnings = int(total_winnings + (bet * 1.5))
                    player_chips = int(player_chips + bet + (bet * 1.5))
                    print("You bet {} chips and won with a Blackjack, so now you have {} chips!".format(bet,
                                                                                                        player_chips))

            else:
                print("\nCongratulations {} you have won this game!".format(player_name))
                player_score = player_score + 1
                if gambling[0].upper() == "Y":
                    total_bet_value = total_bet_value + bet
                    total_winnings = total_winnings + bet
                    player_chips = player_chips + (bet * 2)
                    print("You bet {} chips and won, so now you have {} chips!".format(bet, player_chips))

    play_again(number_of_games, player_name, player_score, dealer_score, player_chips, gambling, total_bet_value,
               total_winnings, total_losses)


game_play(0, "", 0, 0, 500, "", 0, 0, 0)

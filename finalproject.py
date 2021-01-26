from colorama import Fore, Back, Style

a = "\ \ \ "
print('\t\t\t' + Fore.LIGHTMAGENTA_EX, Style.BRIGHT + '--------------------------------------------------')
print('\t\t\t' + Fore.RED, Style.BRIGHT + R'|||         |||  ||\\\      |||      ///    \\\ ')
print('\t\t\t' + Fore.RED, Style.BRIGHT + R'|||         |||  |||\\\     |||    ///        \\\ ')
print('\t\t\t' + Fore.LIGHTBLUE_EX, Style.BRIGHT + R'|||         |||  ||| \\\    |||   ///          \\\ ')
print('\t\t\t' + Fore.LIGHTBLUE_EX, Style.BRIGHT + R'|||         |||  |||  \\\   |||  |||            |||')
print('\t\t\t' + Fore.LIGHTGREEN_EX, Style.BRIGHT + R'|||         |||  |||   \\\  |||  |||            |||')
print('\t\t\t' + Fore.LIGHTGREEN_EX, Style.BRIGHT + R' \\\       ///   |||    \\\ |||   \\\          ///')
print('\t\t\t' + Fore.LIGHTMAGENTA_EX, Style.BRIGHT + R'   \\\    ///    |||     \\\|||    \\\        ///')
print('\t\t\t' + Fore.LIGHTMAGENTA_EX, Style.BRIGHT + R'     \\__//      |||      \\\||      \\\    ///')
print('\t\t\t' + Fore.LIGHTCYAN_EX, Style.BRIGHT + '--------------------------------------------------')
print('\t\t\t\t' + Fore.YELLOW, Style.BRIGHT + "UNO ONLINE: WORLD'S #1 CLASSIC CARD GAME")
print('\t\t\t' + Fore.LIGHTMAGENTA_EX, Style.BRIGHT + '--------------------------------------------------')

import random
import time


def make_deck():
    """
    This function generates an UNO deck consisting of 108 cards.

    A nested for loop is used to combine the card colour and value, in a single string.
    The card (string) is then appended to an empty list 'deck'. Another for loop is used
    to simply append the 'Wild' and 'Wild Draw Four' cards in the list 'deck'.

    Parameters: None
    ----------------
    Return values: deck -> list

    """
    deck = []
    colours = ['Red', 'Blue', 'Green', 'Yellow']
    values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "Draw Two", "Skip", "Reverse"]
    wilds = ["Wild", "Wild Draw Four"]

    for colour in colours:
        for value in values:
            card_val = "{} {}".format(colour, value)
            deck.append(card_val)
            if value != 0:
                # All ordinary cards, except '0' cards are appended twice.
                deck.append(card_val)

    for wild_cards in range(4):
        # In this for loop, both 'Wild' and 'Wild Draw Four' cards are appended four
        # times to the deck.
        deck.append(wilds[0])  # 'Wild' card is appended to the deck here.
        deck.append(wilds[1])  # 'Wild Draw Four' is appended to the deck here.
    return deck


def shuffle_deck(deck):
    """
    This function shuffles a list of items passed into it.

    The position of each card in the list is interchanged with an another card:
    whose position is obtained randomly by using the random module.

    Parameters: deck -> list
    -------------------------
    Return values: deck -> list

    """
    for card_pos in range(len(deck)):
        rand_pos = random.randint(0, 107)
        deck[card_pos], deck[rand_pos] = deck[rand_pos], deck[card_pos]  # swapping the cards
    return deck


def draw_cards(num_of_cards, uno_deck):
    """
    This function draws a specified number of cards off the top of the deck.

    Parameters: num_of_cards -> integer, uno_deck -> list
    ------------------------------------------------
    Return: cards_drawn -> list

    """
    cards_drawn = []
    for deck_card in range(num_of_cards):
        cards_drawn.append(uno_deck.pop(0))
    return cards_drawn


def show_hand(hand):
    """
    This function prints a formatted list of the player's hand.

    Parameter: turn -> string, hand -> list
    ---------------------------------------
    Return: y-1 (total number of cards will be returned as y is incremented
            by 1 after last card so we subtract a 1 from it)

    """
    card_num = 1
    for card in hand:
        print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "{}) {}".format(card_num, card))
        card_num += 1
    print('')
    return (card_num - 1)
    # returns the total number of cards since card_num will be incremented by 1
    # after last iteration so subtract 1 from it


def can_play(discard_pile, hand):
    """
    This function checks whether a player is able to play a card or not.

    The top discard card is split into two strings; one containing the colour
    and the other containing the value of the card. If the user's hand contains
    any 'Wild' or 'Wild Draw Four' card, or a card matching the colour or value
    of the top discard card then this function will return True. Otherwise, it
    will return False.

    Parameters: discard_pile -> list, hand -> list
    ---------------------------------------------
    Return: Boolean value (True or False)

    """
    discard_split = discard_pile[-1].split(' ', 1)  # output: e.g: ['Red','0']
    colour = discard_split[0]  # colour of the card to be picked

    if colour != "Wild":
        value = discard_split[1]
    else:  # Wild cards to have a value 'Any'
        value = 'Any'

    for card in hand:
        if 'Wild' in card:
            # A 'Wild' card is playable at all times, unless it the last card.
            return True
        elif colour in card or value in card:
            # If either the colour or the value of the top discard card matches with
            # any of the cards present in the hand, then the card is valid/playable.
            return True
    # If a player does not have a valid card, then the function will return False.
    return False


def wrong_card(discard_pile, card):
    """
    This function checks whether the user has played a wrong/invalid card.

    If the card played by the player matches the top discard card in colour or value, or
    the card is a 'Wild' or 'Wild Draw Four' card, then this function will return False,
    meaning the player played an valid card. However, if the the player played a invalid
    card, then the function will return True.

    Parameters: discard_pile -> list, card -> string
    ---------------------------------------------
    Return: Boolean value (True or False)

    """
    discard_split = discard_pile[-1].split(' ', 1)
    colour = discard_split[0]
    if colour != "Wild":
        value = discard_split[1]
    else:
        value = 'Any'
    if 'Wild' in card or colour in card or value in card:
        # Player played a valid card.
        return False
    else:
        # Player played an invalid card.
        return True


def pc_check(discard_pile, hand):
    """
    This function checks whether the PC has any valid cards available.

    The top discard card is split into two strings; one containing the colour
    and the other containing the value of the card. If the PC's hand contains
    any 'Wild' or 'Wild Draw Four' card, or a card matching the colour or value
    of the top discard card, then this function will return the index of that
    card in the PC's Hand.

    Parameters: discard_pile -> list, hand -> list
    ----------------------------------------------
    Return: int

    """
    discard_split = discard_pile[-1].split(' ', 1)  # same steps as for the can_play function for player
    colour = discard_split[0]
    if colour != "Wild":
        value = discard_split[1]
    else:
        value = 'Any'
    for card in range(len(hand)):
        if 'Wild' in hand[card] or colour in hand[card] or value in hand[card]:
            return card


def choose_first():
    """
    This function randomly decides which player(Player or PC) will go first.

    Parameters: None
    ----------------
    Return values: str ('PLAYER' or 'PC')

    """
    if random.randint(0, 1) == 0:
        return 'PLAYER'
    else:
        return 'PC'


def invalid_wild(discard_pile, hand):
    """
        This function checks whether the Wild Draw Four played by the user is valid or not.

        The colour and value of the card, played before the Wild draw Four, is compared
        with the the colour and value of each card in the user's hand. If either the colour
        or the value matches, then the function returns True because then that 'Wild draw Four'
        played by the user would an invalid one.

        Parameters: discard_pile -> list, hand -> list
        ------------------------------------------
        Return values: Boolean value (True or False)

        """

    # In this variable, the card played before the Wild Draw Four is stored in the form
    # of a list(containing two strings i.e the card colour and value.)
    discard_split = discard_pile[-2].split(' ', 1)
    for card in hand:
        card_split = card.split(' ', 1)
        if len(card_split) == 1:
            # In case of a 'Wild' card.
            value = 'Any'
        else:
            value = card_split[1]
        if card_split[0] == discard_split[0] or value == discard_split[1]:
            # If either the colour or value of any card in the Player's hand, matches the
            # colour or value of the card played before the 'Wild Draw Four', then the
            # function will return True, and the Player would have to face a penalty for
            # playing an invalid 'Wild Draw Four' card.
            return True
    return False


def pc_challenge(player_hand):
    """
        This function checks whether the Wild Draw Four played by the user is valid or not.

        The colour and value of the card, played before the Wild draw Four, is compared
        with the the colour and value of each card in the user's hand. If either the colour
        or the value matches, then the function returns True because, then that 'Wild draw Four'
        played by the user would an invalid one.

        Parameters: player_hand -> list
        ------------------------------------------------
        Return values: Boolean value (True or False)

        """
    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'PC has challenged your card.\nShow your cards!')
    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'A glimpse of my cards:\n')
    # This for loop displays each of the user's cards momentarily.
    for card in player_hand:
        print(card, end="\r")
        time.sleep(1)
        # This print statement simply overwrites the card displayed with empty character spaces.
        # time.sleep(1) will create a disappearing effect on the print statement
        print(" " * len(card))


def player_challenge(pc_hand):
    """
        This function checks whether the Wild Draw Four played by the PC is valid or not.

        The colour and value of the card, played before the Wild draw Four, is compared
        with the the colour and value of each card in the PC's hand. If either the colour
        or the value matches, then the function returns True because, then that 'Wild draw Four'
        played by the PC would an invalid one.

        Parameters: pc_hand -> list
        ------------------------------------------
        Return values: Boolean value (True or False)

        """
    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\n Player has decided to challenge the card.\n PC must show cards')
    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + "A glimpse of PC's cards:")
    # This for loop displays each of the PC's cards momentarily.
    for card in pc_hand:
        print(card, end="\r")
        time.sleep(1)
        # This print statement simply overwrites the card displayed with empty character spaces.
        print(" " * len(card))


def offer_card(hand):
    """
        This function checks whether or not a player has a valid Action card to offer.

        A single for loop iterates through the (Player's/PC's) hand and checks whether that
        player has an Action card like: Skip, Reverse, Draw Two, Wild or Wild draw Four
        in his hand. If an Action card is found, the function returns True and the respective
        player can then opt for an exchange of cards with the other player.

        Parameters: Hand -> list
        ------------------------------------------
        Return values: Boolean value (True or False)

        """
    for card in hand:
        card_split = card.split(' ', 1)
        if len(card_split) == 1:
            # In case of a 'Wild' card.
            value = 'Any'
        else:
            # The value(number or symbol) of the card is stored in 'value'.
            value = card_split[1]
        if value not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # An Action card was found.
            return True
    # No Action card was found.
    return False


def pc_deal(discard_pile, pc_hand):
    """
        This function checks whether the PC has an Action card in its hand, and offers
        the card to the player in exchange for a card matching the top discard card's
        colour.

        A single for loop iterates through the PC's hand and checks for an Action card
        like: Skip, Reverse, Draw Two, Wild or Wild draw Four. The first Action card
        that is found, is offered to the player. In return, the PC asks for a card
        that matches the colour of the top discard card.

        Parameters: discard_pile -> list, pc_hand -> list
        ----------------------------------------------
        Return values: need_color -> str, card -> str

        """
    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'PC has opted to deal')
    for card in pc_hand:
        card_split = card.split(' ', 1)
        if len(card_split) == 1:
            # In case of a 'Wild' card.
            value = 'Any'
        else:
            # The value(number or symbol) of the card is stored in 'value'.
            value = card_split[1]
        if value not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # PC's hand contains an Action card.
            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'PC offers a "{}"'.format(card), end="")
            break
    discard_split = discard_pile[-1].split(' ', 1)
    need_color = discard_split[0]
    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'and needs a {} colour card in return'.format(need_color))
    time.sleep(1)
    return need_color, card


def player_deal(player_hand, pc_hand):
    """
        This function takes consent from the PC for exchanging cards with the player.

        If the player does not have a valid card to play on his turn, he can request
        to exchange cards with the PC. The player will tell the PC the colour of the
        card he wants, and also the card he is willing to exchange. The PC will
        decide whether or not it wants to exchange cards randomly.

        In case of the PC accepting the player's offer:
        -> If this is the player's last card, then the PC will simply reject the offer.
        -> If the player offers an Action card, then the PC will accept the offer only if it
        has the player's required card in its hand. Otherwise, it will reject the offer.


        Parameters: player_hand -> list, pc_hand -> list
        ----------------------------------------------
        Return values: Boolean value (True or False)

        """
    colours = ['Red', 'Blue', 'Green', 'Yellow']
    required_colour = input('\n What colour card do you want? (first letter capital): ')
    while required_colour not in colours:
        print(' Select from the valid UNO colours (Red/Green/Blue/Yellow) ')
        required_colour = input(Fore.LIGHTBLUE_EX + ' What colour card do you want? (first letter capital): ')
    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + '\n Your cards:\n')
    total_cards = show_hand(player_hand)
    offer = int(input(Fore.LIGHTBLUE_EX + ' Which card do you want to exchange with PC? '))
    while (offer < 1) or (offer > total_cards):
        offer = int(input(Fore.RED + ' Enter valid index for the exchange card: '))

    def pc_consent():
        """
            This function takes consent from the PC for exchanging cards with the player
            by generating a random choice on behalf of the PC.

            Parameters: None
            ----------------------------------------------
            Return values: Boolean value (True or False)

            """
        deal = random.randint(0, 1)
        if deal == 0:
            return True
        else:
            return False

    # If the PC consents to the player's offer.
    if pc_consent():
        offered_card = player_hand[offer - 1].split(' ', 1)
        if len(offered_card) == 1:
            value = 'Any'  # If the player offers a 'Wild' card.
        else:
            value = offered_card[1]

        # If the player offers a number card to the PC instead of an action card then
        # the PC will reject the offer or if the player has one card left PC rejects the offer.
        if len(player_hand) == 1 or value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False

        else:
            # If the player offers an Action card, and the PC also has a card of the player's
            # choice in its hand, then the PC will accept the offer.
            for card in pc_hand:
                # In this for loop, the PC goes through all of its cards to check whether
                # or not it has a card matching the player's specification.
                card_split = card.split(' ', 1)
                if card_split[0] == required_colour:
                    # If the PC finds a card matching the player's specification in its hand,
                    # then it will exchange cards with the player.
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + ' PC is ready to give {}'.format(card))
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + ' Adding {} to your cards..'.format(card))
                    time.sleep(1)
                    print('')
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\nAdding {} to PC\'s cards'.format(player_hand[offer - 1]))
                    pc_hand.append(player_hand[offer - 1])
                    time.sleep(1)
                    return True
            # If the PC does not find a card matching the player's specification in its
            # hand,then it will simply reject the player's offer.
            return False


def last_card_check(hand):
    """
        This function checks whether the last card in a player's hand in an Action card or not.

        If the last card is an Action card like: Skip, Reverse, Draw Two, Wild or Wild Draw Four,
        then the function will return True and the respective player will have to draw a card from
        the discard pile.

        Parameters: hand -> list
        ----------------------------------------------
        Return values: Boolean value (True or False)

        """
    for card in hand:
        card_split = card.split(' ', 1)
        if len(card_split) == 1:
            # In case of a 'Wild' card.
            value = 'Any'
        else:
            value = card_split[1]
        if value not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # If the card is an Action card.
            return True
        else:
            # If the card is a Number card.
            return False


# the main game loop: keeps on executing till the player decides to exit the game
new_game = 'y'
while new_game != 'n':  # 'n' set as sentinel value

    uno_deck = make_deck()  # deck formation
    uno_deck = shuffle_deck(uno_deck)  # deck shuffling
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    colours = ['Red', 'Blue', 'Green', 'Yellow']

    player_hand = []
    pc_hand = []
    # handing both the player and the PC 7 cards each as per UNO rules
    player_hand.extend(
        draw_cards(7, uno_deck))  # draw_cards returns a list so extend is used to add properly it to the player list
    pc_hand.extend(draw_cards(7, uno_deck))

    discard_pile = []
    # The card on top of the UNO deck is placed in the discard pile. This card will now serve as the top card.
    discard_pile.append(uno_deck.pop(0))

    top_split = discard_pile[-1].split(' ',
                                       1)  # .split() creates a list of strings from original string based on the separator
    color = top_split[0]
    if color != "Wild":
        value = top_split[1]
    else:
        value = 'Any'
    if value not in num_list:
        # The game must begin with a number card.
        while value not in num_list:
            discard_pile[-1] = random.choice(discard_pile)

    # Starting turn is decided using the choose_first() function.
    turn = choose_first()
    print()
    print(turn + Fore.LIGHTMAGENTA_EX, Style.BRIGHT + 'WILL GO FIRST\n')

    # this loop will end once either the player or the PC wins
    while (len(player_hand) != 0) or (len(pc_hand) != 0):
        if turn == 'Player':
            time.sleep(1)
            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + "-------------")
            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + "PLAYER'S TURN")
            print(" -------------")
            time.sleep(1)
            print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + " Your hand:")
            print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "---------------------\n")
            total_cards = show_hand(player_hand)
            print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "---------------------")
            if len(player_hand) == 1:  # to make sure that the last card is a non-action card
                if last_card_check(player_hand):
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + ' Last card cannot be an action card!\nAdding one card '
                                                            'from the deck..')
                    time.sleep(1)
                    player_hand.extend(draw_cards(1, uno_deck))
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + ' Your cards:\n')
                    total_cards=show_hand(player_hand)
            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'Card on top of discard pile is: {}'.format(discard_pile[-1]))
            if can_play(discard_pile,
                        player_hand):  # if the player has a valid card in hand then this conditional statement is
                # executed
                card_chosen = int(input(Fore.LIGHTMAGENTA_EX + " Which card do you want to play? "))
                while (card_chosen < 1) or (card_chosen > total_cards):  # dealing with an index out of range
                    card_chosen = int(input(Fore.RED + 'Enter correct index: '))

                while wrong_card(discard_pile, player_hand[card_chosen - 1]):
                    # The player is continuously prompted to play a valid card
                    card_chosen = int(input(Fore.RED + 'Not a valid card. Which card do you want to play? '))

                    while (card_chosen < 1) or (card_chosen > total_cards):
                        card_chosen = int(input(Fore.RED + 'Enter correct index:'))

                print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "You played: {}\n".format(player_hand[card_chosen - 1]))
                time.sleep(1)
                discard_pile.append(player_hand.pop(card_chosen - 1))  # the top card is now the user played card

                # Checking for special cards:
                split_card = discard_pile[-1].split(' ', 1)
                current_colour = split_card[0]
                if current_colour == "Wild":  # conditional statement for the Wild cards
                    if len(split_card) != 1:  # conditional statement will execute for 'Wild Draw Four' only not 'Wild'
                        challenge = random.randint(0,
                                                   1)  # PC randomly decides to challenge the player or to simply proceed
                        if challenge == 0:
                            time.sleep(1.2)
                            pc_challenge(
                                player_hand)  # player will show a glimpse of their cards due to this function call
                            if invalid_wild(discard_pile,
                                            player_hand):  # if foul play detected i.e Wild wrongfully played
                                time.sleep(1.5)
                                print(
                                    Fore.RED + ' => Violation of UNO rule detected. As a penalty, you will draw 6 cards '
                                               'from the deck.')
                                player_hand.extend(draw_cards(6, uno_deck))
                            else:
                                time.sleep(1.5)
                                print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'You played by the rules. PC must draw 4 cards.')
                                print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'Adding 4 cards from deck to PC\'s cards...')
                                time.sleep(1)
                                pc_hand.extend(draw_cards(4, uno_deck))
                        else:
                            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'PC does not want to challenge.')
                            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'Adding 4 cards from deck to PC\'s cards...')
                            time.sleep(1)
                            pc_hand.extend(draw_cards(4, uno_deck))
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\nYou played a Wild card. Have a look at your cards for '
                                                            'colour selection')
                    time.sleep(1)
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "---------------------\n")
                    show_hand(player_hand)
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "---------------------")
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + '\nThese are the available colours:\n')
                    time.sleep(1)
                    for x in range(len(colours)):
                        print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "{}) {}".format(x + 1,
                                              colours[x]))  # printing all the valid UNO colours using list: colours
                    new_colour = int(input(Fore.LIGHTMAGENTA_EX + "\nWhat colour would you like to choose? (Enter "
                                                                  "index): "))
                    while (new_colour < 1) or (new_colour > x + 1):  # dealing with index out of range
                        new_colour = int(input(Fore.RED + 'Enter correct index: '))
                    while new_colour not in list(range(1, len(colours) + 1)):
                        new_colour = int(input(
                            Fore.RED + "=> Invalid colour selected, you won't be able to play further. Select a valid "
                                       "colour: "))
                        while (new_colour < 1) or (new_colour > x + 1):
                            new_colour = int(input(Fore.RED + 'Enter correct index: '))

                    current_colour = colours[new_colour - 1]
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'You selected: {} colour'.format(current_colour))
                    time.sleep(1)
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + '\nYour cards:')
                    num_cards = show_hand(player_hand)  # num_cards is the total no. of cards in player's hand
                    card_choice = int(input(Fore.LIGHTMAGENTA_EX  + "Which card do you want to play? "))
                    while (card_choice < 1) or (card_choice > num_cards):
                        card_choice = int(input(Fore.RED + "=> Incorrect index: Which card do you want to play? "))
                    post_wild_player = player_hand[card_choice - 1].split(' ',
                                                                          1)  # splitting the card played after Wild card
                    card_color = post_wild_player[0]
                    while card_color != current_colour:  # if played card has a colour different from the one selected after playing Wild
                        card_choice = int(input(Fore.RED + '=> Not a valid card. Which card do you want to play? '))
                        while (card_choice < 1) or (card_choice > num_cards):
                            card_choice = int(input(Fore.RED + "=> Incorrect index: Which card do you want to play? "))
                        post_wild_player = player_hand[card_choice - 1].split(' ', 1)
                        card_color = post_wild_player[0]
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "You played {}".format(player_hand[card_choice - 1]))
                    discard_pile.append(player_hand.pop(card_choice - 1))  # top card updated
                    split_card = discard_pile[-1].split(' ', 1)
                if len(split_card) != 1:  # a card other than 'Wild' card
                    card_value = split_card[1]
                else:
                    card_value = 'Any'  # Wild card assigned a value of 'Any'
                if card_value in num_list:  # a number card played
                    turn = 'PC'
                elif card_value == "Reverse":
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\n=> Reversing the game...')
                    time.sleep(1)
                    turn = 'Player'
                elif card_value == "Skip":
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\n=> Skipping PC\'s turn...')
                    time.sleep(1)
                    turn = 'Player'
                elif card_value == "Draw Two":
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\n=> Adding two cards from deck to PC\'s cards..\n')
                    time.sleep(1)
                    pc_hand.extend(draw_cards(2, uno_deck))
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + 'It is Player\'s turn again')
                    turn = 'Player'
                print('')
            else:  # player has no valid card
                time.sleep(1)
                print(Fore.RED + " You can't play.")
                if offer_card(player_hand):
                    # If the Player has an Action card.
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + ' You are in the position of making a deal')
                    option = input(Fore.LIGHTBLUE_EX + ' Deal or Proceed? (d/p): ')
                    while (option != 'd') and (option != 'p'):
                        option = input(Fore.RED + " You can either DEAL or PROCEED! Select an option from d or p: ")
                    if option == 'd':
                        if player_deal(player_hand, pc_hand):  # PC agrees to deal with the Player
                            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '=> Deal successful.')
                        else:
                            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + ' PC rejected the offer. Adding a deck card to '
                                                                    'your cards..')
                            player_hand.extend(draw_cards(1, uno_deck))
                            time.sleep(1)
                            turn = 'PC'
                    else:
                        print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + '\n Adding a card from the deck...')
                        time.sleep(1)
                        player_hand.extend(draw_cards(1, uno_deck))
                        turn = 'PC'
                else:
                    time.sleep(1)
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'DEALS CAN BE MADE BY EXCHANGING AN ACTION CARD WITH A '
                                                            'REQUIRED COLOUR CARD')

                    time.sleep(1)
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\tYou cannot deal right now.\nAdding a card from the '
                                                            'deck...')
                    time.sleep(1.5)
                    player_hand.extend(draw_cards(1, uno_deck))
                    turn = 'PC'
                print('')
            # Checking if player has won:
            if len(player_hand) == 0:  # Player played their last card and now have 0 cards
                winning_player = "Player"
                break
        if turn == 'PC':
            time.sleep(1)
            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + "----------")
            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'PC\'s TURN')
            print(" ----------")
            if len(pc_hand) == 1:
                if last_card_check(pc_hand):
                    # Game can not end with an Action card.
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + ' PC\'s last card is an action card!\n Adding one card from '
                                                            'the deck..')
                    time.sleep(1)
                    pc_hand.extend(draw_cards(1, uno_deck))
            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'Card on top of discard pile is: {}'.format(discard_pile[-1]))
            if can_play(discard_pile, pc_hand):
                # The PC has a valid/playable card in its hand.
                time.sleep(1)
                card_index = pc_check(discard_pile, pc_hand)  # The PC searches for the index of the card.
                print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "PC played: {}".format(pc_hand[card_index]))
                time.sleep(1.5)
                discard_pile.append(pc_hand.pop(card_index))  # PC's played card set as top card

                # Checking for special cards:
                split_card = discard_pile[-1].split(' ', 1)
                current_colour = split_card[0]
                if current_colour == "Wild":
                    if len(split_card) != 1:
                        option = input(Fore.LIGHTBLUE_EX + ' Do you want to challenge this Wild Draw Four card or not? '
                                                           '(y/n): ')
                        while option != 'y' and option != 'n':
                            option = input(Fore.RED + " Say YES or NO! Select an option from y(YES) or n(NO): ")
                        if option == 'y':
                            player_challenge(pc_hand)  # PC shows a glimpse of its cards due to this function call
                            if invalid_wild(discard_pile, pc_hand):  # Wild played wrongfully
                                time.sleep(1.5)
                                print(Fore.RED + ' => PC caught violating UNO rule. As a penalty, it must draw 6 cards '
                                                 'from the deck')
                                time.sleep(1.2)
                                pc_hand.extend(draw_cards(6, uno_deck))
                            else:
                                time.sleep(1)
                                print(
                                    Fore.LIGHTBLUE_EX, Style.BRIGHT + 'PC played by the rules. Player must draw 4 '
                                                                      'cards\n\n Adding 4 cards from deck to Player\'s'
                                                                      ' cards..\n')
                                time.sleep(1)
                                player_hand.extend(draw_cards(4, uno_deck))
                        else:  # option = 'n'
                            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'Player opted not to challenge')
                            player_hand.extend(draw_cards(4, uno_deck))
                    for pc_card in pc_hand:
                        clr_card = pc_card.split(' ', 1)
                        if clr_card[
                            0] == 'Wild':  # Wild cards in pc hand will be ignored as a colour card is required for colour choice
                            continue
                        else:
                            current_colour = clr_card[0]
                            time.sleep(.5)
                            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\tWild card color selection...\n\tPC selects {} '
                                                                    'colour'.format(current_colour))

                            break
                    for new_card in pc_hand:
                        post_wild_pc = new_card.split(' ', 1)
                        if post_wild_pc[0] == current_colour:  # PC plays a card if it matches the PC's selected colour
                            print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "PC played: {}".format(new_card))
                            discard_pile.append(new_card)  # top card updated
                            split_card = discard_pile[-1].split(' ', 1)
                            break
                if len(split_card) != 1:  # a card other than the 'Wild' card
                    card_value = split_card[1]
                else:  # for a Wild card, value will be set as 'Any'
                    card_value = 'Any'
                if card_value in num_list:  # a number card played
                    turn = 'Player'
                if card_value == "Reverse":
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\n=> Reversing the game...')
                    time.sleep(1)
                    turn = 'PC'
                elif card_value == "Skip":
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\n=> Skipping Player\'s turn...')
                    time.sleep(1)
                    turn = 'PC'
                elif card_value == "Draw Two":
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\n=> Adding two cards from deck to Player\'s cards..\n')
                    time.sleep(1)
                    player_hand.extend(draw_cards(2, uno_deck))
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + 'It is PC\'s turn again')
                    turn = 'PC'
                print('')
            else:  # PC doesnot have a valid card
                time.sleep(1.5)
                print(Fore.RED + " PC can't play.")
                time.sleep(1)
                if offer_card(pc_hand):
                    pc_color, deal_card = pc_deal(discard_pile,
                                                  pc_hand)  # pc_color: colour required by PC, deal_card: card
                    # offered by PC
                    print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + '\n Your cards: ')
                    cards_in_playerhand = show_hand(player_hand)
                    option = input(Fore.LIGHTBLUE_EX + '\n Accept offer or Reject offer? (a/r): ')
                    while (option != 'a') and (option != 'r'):
                        option = input(Fore.RED + " You can either ACCEPT or REJECT! Select an option from a or r: ")
                    if option == 'a':
                        deal_cards = []  # creating a list of strings with the split player cards
                        for player_card in player_hand:
                            offer_pc_card = player_card.split(' ', 1)
                            deal_cards.append(offer_pc_card[0])
                        if pc_color not in deal_cards:  # if PC's required card's colour not in player's hand then
                            # Player cannot deal
                            print(Fore.LIGHTBLUE_EX, Style.BRIGHT + " Going through the player's cards...")
                            time.sleep(1)
                            print(
                                Fore.LIGHTBLUE_EX, Style.BRIGHT + '\t Player cannot accept PC\'s deal at the '
                                                                  'moment\n.\n.\n\t Required colour card does not '
                                                                  'exist\n')
                            turn = 'Player'
                        else:
                            give_card = int(input(
                                Fore.LIGHTMAGENTA_EX + ' Select a card for PC: '))  # If player has a card with same colour as PC's required colour card
                            while (give_card < 1) or (give_card > cards_in_playerhand):  # index out of range
                                give_card = int(input(Fore.LIGHTMAGENTA_EX + ' Select a card for PC: '))

                            player_offer_card = player_hand[give_card - 1].split(' ', 1)
                            while player_offer_card[0] != pc_color:  # invalid colour card selected for PC
                                print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'PC wants a {} card!'.format(pc_color))
                                give_card = int(input(Fore.RED + ' Select an appropriate card for PC: '))
                                while (give_card < 1) or (give_card > cards_in_playerhand):
                                    give_card = int(input(Fore.LIGHTMAGENTA_EX + ' Select a card for PC: '))
                                player_offer_card = player_hand[give_card - 1].split(' ', 1)
                            print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "\n Adding {} to PC's cards".format(player_hand[give_card - 1]))
                            time.sleep(1)
                            pc_hand.append(player_hand.pop(give_card - 1))
                            print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + "\n Adding {} to your cards\n".format(deal_card))
                            time.sleep(1)
                            player_hand.append(deal_card)
                            turn = 'Player'
                    else:  # option == 'r'
                        print(Fore.LIGHTBLUE_EX, Style.BRIGHT + 'PC\'s offer rejected.')
                        pc_hand.extend(draw_cards(1, uno_deck))
                        turn = 'Player'
                else:  # if PC doesnot have an action card
                    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + "PC has no offer to make. Adding card to PC's hand...")
                    pc_hand.extend(draw_cards(1, uno_deck))
                    turn = 'Player'
            time.sleep(1)
            print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT + 'PC has {} cards remaining\n'.format(len(pc_hand)))
            # Checking if the PC has won:
            if len(pc_hand) == 0:
                winning_player = "PC"
                break
    # out of the inner while loop
    time.sleep(1.2)
    print(Fore.RED, Style.BRIGHT + "\t\t    GAME OVER")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX, Style.BRIGHT + "\t\t{} is the winner!".format(winning_player))
    print('')
    time.sleep(1)
    new_game = input(Fore.LIGHTBLUE_EX + 'Would you like to play again? (y/n): ')
    while (new_game != 'n') and (new_game != 'y'):  # invalid option selected
        new_game = input(Fore.RED + " PLAY a new game or EXIT! Select an option from y(YES) or n(NO): ")
    if new_game == 'n':
        print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\n\t\tTHANKS FOR PLAYING!')
        break
    else:
        print(Fore.LIGHTBLUE_EX, Style.BRIGHT + '\nStarting a new game..')
        continue
print(Fore.RED, Style.BRIGHT + '\t\t...EXITING UNO...\n')



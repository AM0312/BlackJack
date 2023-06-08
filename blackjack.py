import art
import random
import os


def deal_card():
    '''Deal a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    '''Calculate the blackjack score using the list of cards that 
    player/dealer has.'''
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user, computer):
    '''Compare user and computer score based on blackjack rules.'''
    if user == computer:
        return ("Draw")
    elif computer == 0:
        return ("Computer has BlackJack. It Wins.")
    elif user == 0:
        return ("User has BlackJack. User Wins.")
    elif user > 21:
        return ("User went over. Computer Wins.")
    elif computer > 21:
        return ("Computer went over. User Wins.")
    elif computer > user:
        return ("Computer has higher score. It Wins.")
    else:
        return ("User has higher score. User Wins.")


def blackjack():
    '''Play a game of blackjack with the computer.'''
    print(art.logo)
    is_game_over = False
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards:{user_cards}\nYour Score:{user_score}")
        print(f"Computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Do you want to draw another card? Type y/n:")
            if choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(
        f"\n\nUser's final hand:{user_cards}\nUser's final score:{user_score}")
    print(
        f"\nComputer's final hand:{computer_cards}\nComputer's final score:{computer_score}")
    print(compare(user_score, computer_score))

    if input("Do you want to play a fresh game? Type y/n:") == "y":
        os.system('cls')
        blackjack()
    else:
        print("GoodBye")


blackjack()

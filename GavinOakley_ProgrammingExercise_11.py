import random

#Create the deck class and define the function for dealing and shuffling cards up to a defined deck size.
class Deck():

    def __init__(self, size):
        self.current_deck = [i for i in range(size)]
        random.shuffle(self.current_deck)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.current_deck)
            self.current_card = 0
            print(" -  Reshuffling!")
        self.current_card += 1
        return self.current_deck[self.current_card - 1]

#Define the ranks and suits for the deck.
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♣', '♦', '♥', '♠' ]

#Define the main function which creates a deck of 52 cards from the deck class,
#deals 5 cards from the deck into the hand list, displays the hand, then discards the chosen cards.
def main():
    my_deck = Deck(52)
    hand = [my_deck.deal() for _ in range (5)]

    display_hand(hand)
    discard(hand,my_deck)

#Define the function for displaying the user's hand. Enumerate allows the user to see the number of each card.
def display_hand(hand):
    for number, card in enumerate(hand, start=1):
        r = card % 13
        s = card // 13
        print(number, "-", ranks[r], "of", suits[s])

#Define the function for discarding up to 3 cards from the deck based on user input.
def discard(hand, deck):
    while True:
        choices = (input(" - Select up to 3 cards to discard (1, 2, 3...): "))

        #Begin the try/except block to catch input errors.
        try:
            #User's input is split into just the integers without commas.
            chosen_cards = [int(choice.strip()) for choice in choices.split(",")]
        except ValueError:
            print(" - Please select 3 cards separated by commas (1, 2, 3...): ")
            continue

        #Stops the user from discarding more than 3 cards.
        if not 1 <= len(chosen_cards) <= 3:
            print(" - Please select 3 cards separated by commas (1, 2, 3...): ")
            continue

        #Stops the user from inputting the same card twice.
        if len(set(chosen_cards)) != len(chosen_cards):
            print(" - Please select 3 unique cards (1, 2, 3...): ")

        #Stops the user from inputting a number greater than 5 (max card number).
        if any(number < 1 or number > 5 for number in chosen_cards):
            print(" - Please select 3 cards separated by commas (1, 2, 3...): ")
            continue

        #Finally, replace each discarded card with a new card from the deck.
        for number in chosen_cards:
            hand[number - 1] = deck.deal()

        #Notify the user and display their new deck.
        print(" - Discarding!")
        display_hand(hand)

        #Allow the user to input y to continue discarding, or n to stop.
        while True:
            retry = input(" - Continue discarding? (y/n): ").strip().lower()
            if retry == "y":
                break
            if retry == "n":
                return
            print("- Please enter y or n.")

if __name__ == "__main__":
    main()
#First, set up some constant variables as defaults to be used for counting in both functions.
TICKETS_AVAILABLE = 10
MAX_TICKETS = 4
BUYERS = 0

#Define the function for buying tickets, taking input and printing relevant info.
def buy_tickets():
    #Defining the constant variables as global allows them to be modified in function.
    global TICKETS_AVAILABLE, BUYERS

    while True:
        tickets_bought = int(input("Please enter the amount of tickets to purchase. (Max. 4) : "))

        if tickets_bought > MAX_TICKETS:
            print("Error: Max of 4 tickets per customer. \n")
            continue
        if tickets_bought > TICKETS_AVAILABLE:
            print("Not enough tickets available for purchase. \n")
            continue

        TICKETS_AVAILABLE -= tickets_bought
        BUYERS += 1

        print(f"There are {TICKETS_AVAILABLE} tickets left. \n")
        return

#Define the main function which runs the buy_tickets function as long as there are
#more than 0 tickets.
def main():
    while TICKETS_AVAILABLE > 0:
        buy_tickets()

    print(f"There are no more tickets remaining. \nTotal buyers: {BUYERS}.")

if __name__ == '__main__':
    main()

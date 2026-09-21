#Import string allows us to format the user's input and get rid of punctuation.
import string

SPAM_WORDS = ["free","unlimited","trial","discount","cheap","bonus","claim","winner","signup","click",
              "apply","special","promotion","prize","rates","guaranteed","paid","gift","access","membership",
              "limited","urgent","exclusive","charges","credit","interest","investment","security","certified","offer"]
#Define an empty set to collect spam words from the user's input.
flagged_words = set()

#Define a function to receive user input.
def receive_email():
    input_email = input("Type your message: ")
#Use the lower() and translate() methods to simplify the string and make it easier to find and match spam words.
    message = input_email.lower().translate(str.maketrans("", "", string.punctuation)).split()
#Then return message so the check_spam function can use it.
    return message

def check_spam(message):
#Create the spam_rating counter for each new message and print the list of words after they are added.
    spam_rating = 0
    for word in message:
        if word in SPAM_WORDS:
            spam_rating += 1
            flagged_words.add(word)
    print("Flagged spam-related words: ", list(flagged_words))

#If more than 3 spam words are used, the user is warned of a high likelihood for spam.
    if spam_rating >= 3:
        print(f"Spam rating: {spam_rating}. Likely spam.")
    else: print(f"Spam rating: {spam_rating}.")

def main():
    message = receive_email()
    check_spam(message)

main()
import os

from art import logo

flag = True
highest_paid_person = {
    'name': '',
    'bid-price': 0
}

def clear():
    os.system('clear')

def store_value(name, bid_price):
    highest_paid_person['name'] = name
    highest_paid_person['bid-price'] = bid_price

    return highest_paid_person

# show logo
print(logo)

while flag:
    # ask name and price
    your_name = input('What is your name? \n')
    your_bid_price = input('What is your bid price? $ \n')

    if float(your_bid_price) > float(highest_paid_person['bid-price']):
        # store value in dict
        store_value(your_name, your_bid_price)

    # ask another person
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()

    # finish auction or continue
    if another_bidder == 'yes':
        clear()
    elif another_bidder == 'no':
        flag = False
        winner_name = highest_paid_person['name']
        highest_price = highest_paid_person['bid-price']

        print(f'The winner is {winner_name} with a bid of {highest_price}$')

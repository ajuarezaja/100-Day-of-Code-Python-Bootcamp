from replit import clear
from art import logo

# HINT: You can call clear() to clear the output in the console.

print(logo)
print('Welcome to the secret auction program.')
clear()
bids = []
while True:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    bids.append({"name": name, "bid": bid})
    other_bidders = input('Are ther other bidders? Type yes or no: ').lower()
    if other_bidders != 'yes':
        clear()

        break
    else:
        clear()


bid_amount = 0
for key in range(0,len(bids)):
    if bids[key]["bid"] > bid_amount:
        bid_amount = bids[key]["bid"]
        winner = bids[key]['name']


print(f'The winner is {winner}')




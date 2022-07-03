print("Welcome to the secret auction program.")

dictionary_auction = dict()
finish_bid = False


def auction_winner(participants):
    highest_bid = 0
    win = ""
    for bigger in participants:
        amount_bid = participants[bigger]
        if amount_bid > highest_bid:
            highest_bid = amount_bid
            win = bigger
    print(f"The winner is {win} with a bid of ${highest_bid}")


while not finish_bid:
    name = input("What is your name?: ")
    bid_price = int(input("What is you bid?: $"))
    dictionary_auction["name"] = bid_price
    restart = input("Are there any other bidders? Type: 'yes' or 'no'. \n")
    if restart == "no":
        finish_bid = True
        auction_winner(dictionary_auction)



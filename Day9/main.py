from gavel import logo
print(logo)


print("Welcome to auction house!")

def find_highest_bidder(bid_in_store):
    winner = ""
    highest_bid = 0
    for bidder in bid_in_store:
        bid_amount = bid_in_store[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


store_bid = {}
# print(store_bid)
bidding_action = True
while bidding_action:
    bidders_name = input("What is your name?: ")
    bid_price = int(input("What is your bid price?: $"))
    store_bid[bidders_name] = bid_price 
    other_bidders = input("Are there other people to bid?: Pick 'yes' or 'no'. \n").lower()

    if other_bidders == "no":
        bidding_action = False
        find_highest_bidder(store_bid)
    elif bidding_action == "yes":
        print("\n * 10")

    




        
   

   

    
    
    
        
            









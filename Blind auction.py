import logo

print("Welcome to the Blind Auction Program!")
print(logo.logo)

usernames_and_bids = {}


no_more_users = True
while no_more_users:
    username = input("What is your name?\n")
    bid = int(input("How much, in Naira, are you willing to bid?\n"))
    usernames_and_bids[username] = bid
    users_left = input("Does any other person want to bid? Enter 'y' for yes or 'n' for no:\n").lower()
    
    if users_left == "n":
        no_more_users = False
        print("We have come to the end of this bidding program.")
        f = 0
        for i in usernames_and_bids:
            if f < usernames_and_bids[i]:
                f = usernames_and_bids[i]
        for key, value in usernames_and_bids.items():
            if value == f:
                print(f"The winner of this bid is: {key} with a bid of #{f}.")
        break
        
    elif users_left == "y":
        print("\n" * 250)
       
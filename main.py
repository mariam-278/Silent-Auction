from art import logo
print(logo)

players = {}
should_continue = True

while should_continue:
    username = input("What is your name?\n")
    bid_price = int(input("What is your bid price? £"))

    players[username] = bid_price

    extra_players = input("Are there other bidders? Type 'yes' or 'no'.\n").lower()

    if extra_players == "yes":
        print("\n" * 100)
    else:
        should_continue = False


print(f"The highest bidder is {max(players, key=players.get)}")
import os
import art


def clear():
    os.system("cls" if os.name == "nt" else "clear")


more_bidders = True

bidders = {}
clear()

while more_bidders:
    print(art.logo)
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bid = round(bid, 2)
    if name in bidders.keys():
        print("Bid not captured, already a bidder with this name")
    else:
        bidders[name] = bid

    more = input("Are there more bidders ('y' or 'n')? ").lower()
    if more not in ["y", "n"]:
        print("invalid input..we'll assume more bidders")
    elif more == "n":
        more_bidders = False
    clear()

high_bid = {"name": "No Winner", "bid": 0}

for k, v in bidders.items():
    if v > high_bid["bid"]:
        high_bid["name"] = k
        high_bid["bid"] = v

print(
    f"The high bid is {high_bid['name']} with a bid of ${high_bid['bid']:.2f}"
)

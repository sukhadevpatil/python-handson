bids = {}

bid_continue = True


def find_bid_winner(bids_data):
    max_bid = 0
    bid_winner = ''
    for bidder_name in bids_data:
        amt = bids_data[bidder_name]
        if amt > max_bid:
            max_bid = amt
            bid_winner = bidder_name

    print(f"Bid winner is {bid_winner} with amount ${max_bid}")


while bid_continue:
    name = input('What is your name ? ')
    amount = input('Enter your Bid Amount ? $')
    bids[name] = int(amount)
    more_bid = input('You want to bid more ? [enter "yes" or "no"] : ')

    if more_bid == 'yes':
        bid_continue = True
    if more_bid == 'no':
        bid_continue = False
        find_bid_winner(bids)

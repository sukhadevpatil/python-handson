
bids = {}

bid_continue = True


def find_bid_winner(bids_data):
    max_bid = 0
    bid_winner = ''
    for name in bids_data:
        amount = bids_data[name]
        if amount > max_bid:
            max_bid = amount
            bid_winner = name

    print(f"Bid winner is {name} with amount ${max_bid}")



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






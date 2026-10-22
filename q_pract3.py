def compute_running_balances(starting_balance, transaction):
    running_history =[]
    current_balance = starting_balance

    for tx in transaction:
        current_balance += tx
        running_history.append(current_balance)

    return running_history

if __name__ == "__main__":
    start = 100
    txs = [25,-50,200,-30]
    print(compute_running_balances(start,txs))




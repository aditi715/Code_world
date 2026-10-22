def find_low_stock_position( stock_levels , threshold):
    alert_indices = []

    for index, stock in enumerate(stock_levels):
        if stock< threshold:
            alert_indices.append(index)

    return alert_indices        

if __name__ == '__main__':
    stocks = [150,45,80,23,190,12]
    thresh = 50
    print(find_low_stock_position(stocks, thresh))
 
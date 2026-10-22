def calcuate_invoice_total(prices):
    valid_total =0.0

    for price in prices:
        if price > 0:
            valid_total += price
            
    final_total = valid_total * 1.05
    return round(final_total , 2)

if __name__ == " __main__":
    sample_input = [10.00, -5.50,20.00,0.00,15.00] 
    print(calcuate_invoice_total(sample_input))


       
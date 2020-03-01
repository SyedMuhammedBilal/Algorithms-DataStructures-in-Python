stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices):
    
    max_profit = 0
    for outer_time in range (len(stock_prices)):
        for inner_time in range (len(stock_prices)):
            
            earlier_time = min(outer_time, inner_time)
            later_time = max(outer_time, inner_time)
            
            earlier_price = stock_prices[earlier_time]
            later_price = stock_prices[later_time]
            
            potential_profit = later_price - earlier_price
            
            max_profit = max(max_profit, potential_profit)
    
    return max_profit


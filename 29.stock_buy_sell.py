# Challenge: You should buy the stock when it is the cheapest and sell it at its most expensive

# Challenge found here: https://app.programiz.pro/community-challenges/preview/stock-buy-sell/info

def maximize_profit(prices):
    # Pre built in min and max
    mini = min(prices)
    maxi = max(prices)

    #return (mini, maxi)

    # ALT to above
    miniVal = 0
    maxVal = 0

    # for every price in the list
    for v in prices:
        # if first item in the list set price
        if (miniVal == 0 and maxVal == 0 and (0 not in prices)):
            miniVal = v
            maxVal = v
        # else if the price is smaller then minimum value or bigger than max value assign to relevant variable
        if (v < miniVal):
            miniVal = v
        if (v > maxVal):
            maxVal = v
    
    # return the min and max val like a tuple
    return (miniVal, maxVal)



if __name__ == "__main__":
    print(maximize_profit([100, 180, 260, 310, 40, 535, 695])) # (40, 695)
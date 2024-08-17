import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    # Calculate the price as the average of bid_price and ask_price
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    if price_b == 0:
        return None  # Handle division by zero
    return price_a / price_b

# Main
if __name__ == "__main__":
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print(f"Quoted {stock} at (bid:{bid_price}, ask:{ask_price}, price:{price})")

        # Assuming the two stocks are named 'A' and 'B'
        price_a = prices.get('A')
        price_b = prices.get('B')

        if price_a is not None and price_b is not None:
            ratio = getRatio(price_a, price_b)
            print(f"Ratio A/B: {ratio}")

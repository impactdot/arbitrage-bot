import ccxt

# Connect to the exchange
exchange = ccxt.binance()

# Set the symbol you want to get the price for
symbol = "BTC/USDT"

# Retrieve the latest price
price = exchange.fetch_ticker(symbol)["last"]

print(f"The latest price of {symbol} is {price}")

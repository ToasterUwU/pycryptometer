# pycryptometer - API Wrapper for cryptometer.io

This is a small API Wrapper. It contains all the API endpoints that exist in the moment i write this. (18.09.2020 - www.cryptometer.io/api-doc)


# Usage

## Installing the package:

```pip install pycryptometer```

## Using it:

```py
from pycryptometer import Cryptometer

c = Cryptometer("YOUR_API_KEY")
example = c.ANY_OF_THE_FUNCTIONS(THE_ARGS_IT_NEEDS)

print(example.success, example.error, example.data)
```

# The Docs

## The _Response Object:


Every function returns a Object with 3 Properties: success, error and data.

- Success (True or False):  Shows if the API call was successfull.
- Error (None or String):   Contains the error that occured if "success" is False.
- Data (Array or Dict):     Contains the data that the API gave back.
#
## The Cryptometer Class:

### The Arguments:

- exchange: (String) The name of the trading website. Example: "Binance"

- market_pair: (String) Pair of Currencys. Each exchange has his own pairs. You can find them by using market_list()

- pair: (String) Almost like market_pair. I dont really know why there are two different of these. You can find them by using market_list()

- coin: (String) A Cryptocurrency. Example: BTC, XRP or XMR. Can also found with market_list()

- timeframe: (String) A timeframe, thats it. All possible Values: 5m, 15m, 30m, 1h, 4h, d

- exchange_type: (String) Can be either "spot" or "futures"

- source: (String) Can be "open", "close", "high", "low" or "volume"

- period: (Integer) Between 1 and 300. The official docs dont give a explanation what this is or what it does.

#

### The functions:
- market_list(exchange) -> returns all market_pair's of the exchange

- tickerlist(exchange) -> returns value and change data for every market_pair

- single_ticker(exchange, market_pair) -> returns the same as tickerlist() but only for one market_pair

- trend_indicator() -> returns "trend_score", "buy_pressure", "sell_pressure" and "timestamp"

- btc_liquidation() -> returns "longs" and "shorts" for BTC

- bitmex_liquidation(market_pair) -> returns Buy and Sell data with "market_pair", "quantity", "side" (SELL or BUY) and "timestamp"

- rapid_movements() -> returns all detected rapid movements of all exchanges

- trade_volume_24h(exchange, pair) -> returns "buy" and "sell"

- today_merged_volume(coin) -> returns "buy", "sell" and "timestamp"

- today_longs_shorts(exchange, coin) -> returns the longs and shorts of a coin from one exchange

- hourly_buy_sell_volume(coin) -> returns the buy and sell volume of the last 24 hours in 24 values - 1 value per hour

- merged_buy_sell_volume(coin, timeframe, exchange_type) -> returns the buy and sell volume of a coin merged from all exchanges in a specific timeframe and with a specific exchange_type

- indicator_sma(exchange, market_pair, timeframe, source, period) -> This gives various floats back that are the values of that indicator

- open_interest(exchange, market_pair) -> returns the open interest of one coin on one exchange

- merged_orderbook -> returns all bids and ask values merged from all exchanges

# Help and Suggestions

For help with this libary, bugs you found or suggestions you can write a Issue or join my Discord: https://discord.gg/QuqaCuF

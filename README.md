[![Downloads](https://pepy.tech/badge/pycryptometer)](https://pepy.tech/project/pycryptometer)

# pycryptometer - API Wrapper for "cryptometer.io"

This is a small API Wrapper. It contains all the API endpoints that exist. This package will be updated whenever there are new endpoints.


# Usage

## Installing the package:

```pip install pycryptometer```

## Using it:

```py
from pycryptometer import Cryptometer

c = Cryptometer("YOUR_API_KEY")
syntax = c.ANY_OF_THE_CATEGORIES.ANY_OF_THE_FUNCTIONS(THE_ARGS_IT_NEEDS)
example = c.infos.market_list("binance")
```
Every function will return either of the following things:

- list
- dictonary
- list filled with dictonarys
- dictonary filles with lists

# The Cryptometer Class:

### **The Arguments:**

- exchange: (String) The name of the trading website. Example: "Binance"

- market_pair: (String) Pair of Currencys. Each exchange has his own pairs. You can find them by using market_list()

- pair: (String) Almost like market_pair, but generalized by "cryptometer.io". You can find them by using market_list()

- coin: (String) A Cryptocurrency. Example: BTC, XRP or XMR. Can also found with market_list()

- timeframe: (String) A timeframe, thats it. All possible Values: 5m, 15m, 30m, 1h, 4h, d

- exchange_type: (String) Can be either "spot" or "futures"

- source: (String) Can be "open", "close", "high", "low" or "volume"

- period: (Integer) Between 1 and 300. A period in days that a indicator uses to display data.

- long_period: (Integer) Same rules and usage as "period"

- short_period: (Integer) Same rules and usage as "period"

- signal_period: (Integer) Same rules and usage as "period"



### **The functions:**

    Big Font: Premium only function

- **infos**:

    - market_list(exchange) -> returns all market_pair's of the exchange

    - tickerlist(exchange) -> returns value and change data for every market_pair

    - single_ticker(exchange, market_pair) -> returns the same as tickerlist() but only for one market_pair

    - today_longs_shorts(exchange, coin) -> returns the longs and shorts of a coin from one exchange

    - open_interest(exchange, market_pair) -> returns the open interest of one coin on one exchange

    - merged_orderbook() -> returns all bids and ask values merged from all exchanges

    - **whale_trades(exchange, symbol) -> returns executed large trades of one exchange**

    - rapid_movements() -> returns all detected rapid movements of all exchanges

- **indicators**:

    - trend() -> returns "trend_score", "buy_pressure", "sell_pressure" and "timestamp"

    - **sma(exchange, market_pair, timeframe, source, period) -> Simple Moving Average**

    - **atr(exchange, market_pair, timeframe, period) -> Average True Range**

    - **psar(exchange, market_pair, timeframe, source, period) -> Parabolic Stop And Reverse**

    - **ema(exchange, market_pair, timeframe, source, period) -> Exponential Moving Average**
    
    - **rsi(exchange, market_pair, timeframe, source, period) -> Relative Strength Index**

    - **cci(exchange, market_pair, timeframe, period) -> Commodity Channel Index**

    - **macd(exchange, market_pair, timeframe, source, long_period, short_period, signal_period) -> Moving Average Convergence Divergence**

- **liquidations**:

    - btc() -> returns "longs" and "shorts" for BTC

    - bitmex(market_pair) -> returns Buy and Sell data with "market_pair", "quantity", "side" (SELL or BUY) and "timestamp"

- **volumes**:

    - today_trade_volume(exchange, pair) -> returns "buy" and "sell"

    - today_merged_volume(coin) -> returns "buy", "sell" and "timestamp"

    - **hourly_buy_sell_volume(coin) -> returns the buy and sell volume of the last 24 hours in 24 values - 1 value per hour**

    - **merged_buy_sell_volume(coin, timeframe, exchange_type) -> returns the buy and sell volume of a coin merged from all exchanges in a specific timeframe and with a specific exchange_type**

# Help and Suggestions

For help with this libary, bugs you found or suggestions you can write a Issue or join my Discord: https://discord.gg/QuqaCuF

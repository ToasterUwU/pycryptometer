import pycryptometer
import time

test = pycryptometer.Cryptometer('YOUR_API_KEY')

#infos
print(test.infos.market_list("binance"))
print(test.infos.tickerlist("binance"))
print(test.infos.single_ticker("binance", "BTC-USDT"))
print(test.infos.today_longs_shorts("binance", "BTC"))
print(test.infos.open_interest("binance", "BTC-USDT"))
print(test.infos.merged_orderbook())
print(test.infos.whale_trades("binance", "BTC"))
print(test.infos.rapid_movements())
print(test.infos.coin_info("binance", "all"))

#Indicators
time.sleep(5) #pausing for not breaking the rule of 10 requests in 5 seconds
print(test.indicators.trend())
print(test.indicators.sma("binance", "BTC-USDT", "4h", "open", 200))
print(test.indicators.atr("binance", "BTC-USDT", "4h", 200))
print(test.indicators.psar("binance", "BTC-USDT", "4h", "open", 200))
print(test.indicators.ema("binance", "BTC-USDT", "4h", "open", 200))
print(test.indicators.rsi("binance", "BTC-USDT", "4h", "open", 200))
print(test.indicators.cci("binance", "BTC-USDT", "4h", 200))
print(test.indicators.macd("binance", "BTC-USDT", "4h", "open", 200, 100, 50))

#liquidations
time.sleep(5)
print(test.liquidations.btc())
print(test.liquidations.bitmex("BTCUSD"))

#volumes
time.sleep(5)
print(test.volumes.today_trade_volume("binance", "BTC-USD"))
print(test.volumes.today_merged_volume("BTC"))
print(test.volumes.hourly_buy_sell_volume("BTC"))
print(test.volumes.merged_buy_sell_volume("BTC", "4h", "futures"))
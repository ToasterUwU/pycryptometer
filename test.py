import pycryptometer
import time

test = pycryptometer.Cryptometer('9bPCg52Z2Gl9VHN1ze1yFVHIJ85qN6WtRoRlP00j')

#infos
print(test.infos.market_list("binance"))

#Indicators
time.sleep(5)
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
print(test.volumes.hourly_buy_sell_volume("BTC"))
print(test.volumes.merged_buy_sell_volume("BTC", "4h", "futures"))
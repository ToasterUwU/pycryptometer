import requests
import json
class Cryptometer():
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.cryptometer.io"

    class _Response():
        def __init__(self, **args):
            self.no_data_errors = [
                "No Data",
                "No Liquidation"
            ]

            self.success = args["success"]
            self.error = args["error"]
            if "data" in args:
                self.data = args["data"]
            else:
                self.data = []

            if self.success == "true":
                self.success = True
            else:
                self.success = False

            if self.error == "false":
                self.error = False
            else:
                if args["error"] not in self.no_data_errors:
                    raise Exception(self.error)
                else:
                    self.success = True

    def _casefold(self, exchange=None, market_pair=None, pair=None, coin=None, timeframe=None, exchange_type=None, source=None, period=None):
        args = {}
        if exchange != None:
            args.update({"e": exchange.lower()})
        if market_pair != None:
            args.update({"market_pair": market_pair.replace("-", "").upper()})
        if pair != None:
            args.update({"pair": pair.replace("-", "").upper()})
        if coin != None:
            args.update({"symbol": coin.upper()})
        if timeframe != None:
            args.update({"timeframe": timeframe.lower()})
        if exchange_type != None:
            args.update({"exchange_type": exchange_type.lower()})
        if source != None:
            args.update({"source": source.lower()})
        if period != None:
            args.update({"period": period})
        return args

    def _send_request(self, endpoint:str, arguments:dict={}):
        args = ["api_key="+self.api_key]

        for x in arguments.items():
            args.append(x[0]+"="+x[1])

        url = self.api_url+endpoint+"?"+"&".join(args)
        r = requests.get(url)
        return self._Response(**json.loads(r.content.decode()))

    def market_list(self, exchange:str):
        endpoint = "/coinlist"
        args = self._casefold(exchange=exchange)
        return self._send_request(endpoint, args)
    
    def tickerlist(self, exchange:str):
        endpoint = "/tickerlist"
        args = self._casefold(exchange=exchange)
        return self._send_request(endpoint, args)
    
    def single_ticker(self, exchange:str, market_pair:str):
        endpoint = "/ticker"
        args = self._casefold(exchange=exchange, market_pair=market_pair)
        return self._send_request(endpoint, args)

    def trend_indicator(self):
        endpoint = "/trend-indicator-v3"
        return self._send_request(endpoint)

    def btc_liquidation(self):
        endpoint = "/liquidation-data"
        return self._send_request(endpoint)

    def bitmex_liquidation(self, market_pair:str):
        endpoint = "/bitmex-liquidation"
        args = self._casefold(market_pair=market_pair)
        return self._send_request(endpoint, args)
    
    def rapid_movements(self):
        endpoint = "/rapid-movements"
        return self._send_request(endpoint)

    def trade_volume_24h(self, exchange:str, market_pair:str):
        endpoint = "/24h-trade-volume-v2"
        args = self._casefold(exchange=exchange, pair=market_pair)
        return self._send_request(endpoint, args)

    def today_merged_volume(self, coin:str):
        endpoint = "/current-day-merged-volume-v2"
        args = self._casefold(coin=coin)
        return self._send_request(endpoint, args)

    def today_longs_shorts(self, exchange:str, coin:str):
        endpoint = "/current-day-long-short-v2"
        args = self._casefold(exchange=exchange, coin=coin)
        return self._send_request(endpoint, args)

    def hourly_buy_sell_volume(self, coin:str):
        endpoint = "/hourly-buy-sell-merged-volume"
        args = self._casefold(coin=coin)
        return self._send_request(endpoint, args)

    def merged_buy_sell_volume(self, coin:str, timeframe:str, exchange_type:str):
        endpoint = "/merged-trade-volume"
        args = self._casefold(coin=coin, timeframe=timeframe, exchange_type=exchange_type)
        return self._send_request(endpoint, args)

    def indicator_sma(self, exchange:str, market_pair:str, timeframe:str, source:str, period:int):
        endpoint = "/indicator-sma"
        args = self._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, source=source, period=period)
        return self._send_request(endpoint, args)

    def open_interest(self, exchange:str, market_pair:str):
        endpoint = "/open-interest"
        args = self._casefold(exchange=exchange, market_pair=market_pair)
        return self._send_request(endpoint, args)
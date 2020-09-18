class Cryptometer():
    def __init__(self, api_key):
        self._api_key = api_key
        self._api_url = "https://api.cryptometer.io"

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
                self.error = None
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
            args.update({"period": str(period)})
        return args

    def _send_request(self, endpoint:str, arguments:dict={}):
        import requests
        import json
        
        args = ["api_key="+self._api_key]

        for x in arguments.items():
            args.append(x[0]+"="+x[1])

        url = self._api_url+endpoint+"?"+"&".join(args)
        r = requests.get(url)
        return self._Response(**json.loads(r.content.decode()))

    def market_list(self, exchange:str):
        '''
        returns all market_pair's of the exchange.


        exchange: Exchange Platform like "binance"
        '''
        endpoint = "/coinlist"
        args = self._casefold(exchange=exchange)
        return self._send_request(endpoint, args)
    
    def tickerlist(self, exchange:str):
        '''
        returns value and change data for every market_pair


        exchange: Exchange Platform like "binance"
        '''
        endpoint = "/tickerlist"
        args = self._casefold(exchange=exchange)
        return self._send_request(endpoint, args)
    
    def single_ticker(self, exchange:str, market_pair:str):
        '''
        returns the same as tickerlist() but only for one market_pair


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()
        '''
        endpoint = "/ticker"
        args = self._casefold(exchange=exchange, market_pair=market_pair)
        return self._send_request(endpoint, args)

    def trend_indicator(self):
        '''
        returns "trend_score", "buy_pressure", "sell_pressure" and "timestamp"
        '''
        endpoint = "/trend-indicator-v3"
        return self._send_request(endpoint)

    def btc_liquidation(self):
        '''
        returns "longs" and "shorts" for BTC
        '''
        endpoint = "/liquidation-data"
        return self._send_request(endpoint)

    def bitmex_liquidation(self, market_pair:str):
        '''
        returns Buy and Sell data with "market_pair", "quantity", "side" (SELL or BUY) and "timestamp"


        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()
        '''
        endpoint = "/bitmex-liquidation"
        args = self._casefold(market_pair=market_pair)
        return self._send_request(endpoint, args)
    
    def rapid_movements(self):
        '''
        returns all detected rapid movements of all exchanges
        '''
        endpoint = "/rapid-movements"
        return self._send_request(endpoint)

    def trade_volume_24h(self, exchange:str, pair:str):
        '''
        returns "buy" and "sell"


        exchange: Exchange Platform like "binance"

        pair: Almost like market_pair. I dont really know why there are two different of these. 
        You can find them by using market_list()
        '''
        endpoint = "/24h-trade-volume-v2"
        args = self._casefold(exchange=exchange, pair=pair)
        return self._send_request(endpoint, args)

    def today_merged_volume(self, coin:str):
        '''
        returns "buy", "sell" and "timestamp"


        coin: A Cryptocurrency. Example: BTC, XRP or XMR. Can also be found with market_list()
        '''
        endpoint = "/current-day-merged-volume-v2"
        args = self._casefold(coin=coin)
        return self._send_request(endpoint, args)

    def today_longs_shorts(self, exchange:str, coin:str):
        '''
        returns the longs and shorts of a coin from one exchange


        exchange: Exchange Platform like "binance"

        coin: A Cryptocurrency. Example: BTC, XRP or XMR. Can also be found with market_list()
        '''
        endpoint = "/current-day-long-short-v2"
        args = self._casefold(exchange=exchange, coin=coin)
        return self._send_request(endpoint, args)

    def hourly_buy_sell_volume(self, coin:str):
        '''
        PREMIUM FEATURE
        returns the buy and sell volume of the last 24 hours in 24 values - 1 value per hour


        coin: A Cryptocurrency. Example: BTC, XRP or XMR. Can also be found with market_list()
        '''
        endpoint = "/hourly-buy-sell-merged-volume"
        args = self._casefold(coin=coin)
        return self._send_request(endpoint, args)

    def merged_buy_sell_volume(self, coin:str, timeframe:str, exchange_type:str):
        '''
        PREMIUM FEATURE
        returns the buy and sell volume of a coin merged from all exchanges in a specific timeframe 
        and with a specific exchange_type


        coin: A Cryptocurrency. Example: BTC, XRP or XMR. Can also be found with market_list()

        timeframe: All possible Values -> 5m, 15m, 30m, 1h, 4h and d

        exchange_type: Can be either "spot" or "futures"
        '''
        endpoint = "/merged-trade-volume"
        args = self._casefold(coin=coin, timeframe=timeframe, exchange_type=exchange_type)
        return self._send_request(endpoint, args)

    def indicator_sma(self, exchange:str, market_pair:str, timeframe:str, source:str, period:int):
        '''
        PREMIUM FEATURE
        SMA -> Simple Moving Average
        This gives various floats back that are the values of that indicator


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()

        timeframe: All possible Values -> 5m, 15m, 30m, 1h, 4h and d

        source: Can be "open", "close", "high", "low" or "volume"

        period: Between 1 and 300. The official docs dont give a explanation what this is or what it does.
        '''
        endpoint = "/indicator-sma"
        args = self._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, source=source, period=period)
        return self._send_request(endpoint, args)

    def open_interest(self, exchange:str, market_pair:str):
        '''
        returns the open interest of one coin on one exchange


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()
        '''
        endpoint = "/open-interest"
        args = self._casefold(exchange=exchange, market_pair=market_pair)
        return self._send_request(endpoint, args)

    def merged_orderbook(self):
        '''
        returns all bids and ask values merged from all exchanges
        '''
        endpoint = "/merged-orderbook"
        return self._send_request(endpoint)
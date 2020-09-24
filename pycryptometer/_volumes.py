class _Volumes():
    def __init__(self, parent):
        self._parent = parent
    
    def trade_volume_24h(self, exchange:str, pair:str):
        '''
        returns "buy" and "sell"


        exchange: Exchange Platform like "binance"

        pair: Almost like market_pair. I dont really know why there are two different of these. 
        You can find them by using market_list()
        '''
        endpoint = "/24h-trade-volume-v2"
        args = self._parent._casefold(exchange=exchange, pair=pair)
        return self._parent._send_request(endpoint, args)

    def today_merged_volume(self, coin:str):
        '''
        returns "buy", "sell" and "timestamp"


        coin: A Cryptocurrency. Example: BTC, XRP or XMR. Can also be found with market_list()
        '''
        endpoint = "/current-day-merged-volume-v2"
        args = self._parent._casefold(coin=coin)
        return self._parent._send_request(endpoint, args)

    def hourly_buy_sell_volume(self, coin:str):
        '''
        PREMIUM FEATURE
        returns the buy and sell volume of the last 24 hours in 24 values - 1 value per hour


        coin: A Cryptocurrency. Example: BTC, XRP or XMR. Can also be found with market_list()
        '''
        endpoint = "/hourly-buy-sell-merged-volume"
        args = self._parent._casefold(coin=coin)
        return self._parent._send_request(endpoint, args)

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
        args = self._parent._casefold(coin=coin, timeframe=timeframe, exchange_type=exchange_type)
        return self._parent._send_request(endpoint, args)

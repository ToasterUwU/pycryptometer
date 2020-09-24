class _Indicators():
    def __init__(self, parent):
        self._parent = parent
    
    def trend_indicator(self):
        '''
        returns "trend_score", "buy_pressure", "sell_pressure" and "timestamp"
        '''
        endpoint = "/trend-indicator-v3"
        return self._parent._send_request(endpoint)

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
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, source=source, period=period)
        return self._parent._send_request(endpoint, args)

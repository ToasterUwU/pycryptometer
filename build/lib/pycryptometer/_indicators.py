class _Indicators():
    def __init__(self, parent):
        self._parent = parent
    
    def trend(self):
        '''
        returns "trend_score", "buy_pressure", "sell_pressure" and "timestamp"
        '''
        endpoint = "/trend-indicator-v3"
        return self._parent._send_request(endpoint)

    def sma(self, exchange:str, market_pair:str, timeframe:str, source:str, period:int):
        '''
        PREMIUM FEATURE
        SMA -> Simple Moving Average


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

    def atr(self, exchange:str, market_pair:str, timeframe:str, period:int):
        """
        PREMIUM FEATURE
        ATR -> Average True Range


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()

        timeframe: All possible Values -> 5m, 15m, 30m, 1h, 4h and d

        period: Between 1 and 300. The official docs dont give a explanation what this is or what it does.
        """
        endpoint = "/indicator-atr"
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, period=period)
        return self._parent._send_request(endpoint, args)

    def psar(self, exchange:str, market_pair:str, timeframe:str, source:str, period:int):
        """
        PREMIUM FEATURE
        PSAR -> Parabolic Stop And Reverse


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()

        timeframe: All possible Values -> 5m, 15m, 30m, 1h, 4h and d

        source: Can be "open", "close", "high", "low" or "volume"

        period: Between 1 and 300. The official docs dont give a explanation what this is or what it does.
        """
        endpoint = "/indicator-psar"
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, source=source, period=period)
        return self._parent._send_request(endpoint, args)

    def ema(self, exchange:str, market_pair:str, timeframe:str, source:str, period:int):
        """
        PREMIUM FEATURE
        EMA -> Exponential Moving Average


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()

        timeframe: All possible Values -> 5m, 15m, 30m, 1h, 4h and d

        source: Can be "open", "close", "high", "low" or "volume"

        period: Between 1 and 300. The official docs dont give a explanation what this is or what it does.
        """
        endpoint = "/indicator-ema"
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, source=source, period=period)
        return self._parent._send_request(endpoint, args)

    def rsi(self, exchange:str, market_pair:str, timeframe:str, source:str, period:int):
        """
        PREMIUM FEATURE
        RSI -> Relative Strength Index


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()

        timeframe: All possible Values -> 5m, 15m, 30m, 1h, 4h and d

        source: Can be "open", "close", "high", "low" or "volume"

        period: Between 1 and 300. The official docs dont give a explanation what this is or what it does.
        """
        endpoint = "/indicator-rsi"
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, source=source, period=period)
        return self._parent._send_request(endpoint, args)

    def cci(self, exchange:str, market_pair:str, timeframe:str, period:int):
        """
        PREMIUM FEATURE
        CCI -> Commodity Channel Index


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()

        timeframe: All possible Values -> 5m, 15m, 30m, 1h, 4h and d

        period: Between 1 and 300. The official docs dont give a explanation what this is or what it does.
        """
        endpoint = "/indicator-cci"
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, period=period)
        return self._parent._send_request(endpoint, args)

    def macd(self, exchange:str, market_pair:str, timeframe:str, source:str, long_period:int, short_period:int, signal_period:int):
        """
        PREMIUM FEATURE
        MACD -> Moving Average Convergence Divergence


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()

        timeframe: All possible Values -> 5m, 15m, 30m, 1h, 4h and d

        period: Between 1 and 300. The official docs dont give a explanation what this is or what it does.

        long_period: Same rules and usage as "period"

        short_period: Same rules and usage as "period"

        signal_period: Same rules and usage as "period"
        """
        endpoint = "/indicator-macd"
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair, timeframe=timeframe, source=source, long_period=long_period, short_period=short_period, signal_period=signal_period)
        return self._parent._send_request(endpoint, args)

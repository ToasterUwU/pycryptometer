class _Infos():
    def __init__(self, parent):
        self._parent = parent

    def market_list(self, exchange:str):
        '''
        returns all market_pair's of the exchange.


        exchange: Exchange Platform like "binance"
        '''
        endpoint = "/coinlist"
        args = self._parent._casefold(exchange=exchange)
        return self._parent._send_request(endpoint, args)

    def tickerlist(self, exchange:str):
        '''
        returns value and change data for every market_pair


        exchange: Exchange Platform like "binance"
        '''
        endpoint = "/tickerlist"
        args = self._parent._casefold(exchange=exchange)
        return self._parent._send_request(endpoint, args)

    def single_ticker(self, exchange:str, market_pair:str):
        '''
        returns the same as tickerlist() but only for one market_pair


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()
        '''
        endpoint = "/ticker"
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair)
        return self._parent._send_request(endpoint, args)

    def today_longs_shorts(self, exchange:str, coin:str):
        '''
        returns the longs and shorts of a coin from one exchange


        exchange: Exchange Platform like "binance"

        coin: A Cryptocurrency. Example: BTC, XRP or XMR. Can also be found with market_list()
        '''
        endpoint = "/current-day-long-short-v2"
        args = self._parent._casefold(exchange=exchange, coin=coin)
        return self._parent._send_request(endpoint, args)

    def rapid_movements(self):
        '''
        returns all detected rapid movements of all exchanges
        '''
        endpoint = "/rapid-movements"
        return self._parent._send_request(endpoint)

    def open_interest(self, exchange:str, market_pair:str):
        '''
        returns the open interest of one coin on one exchange


        exchange: Exchange Platform like "binance"

        market_pair: Pair of Currencys. Each exchange has his own pairs. 
        You can find them by using market_list()
        '''
        endpoint = "/open-interest"
        args = self._parent._casefold(exchange=exchange, market_pair=market_pair)
        return self._parent._send_request(endpoint, args)

    def merged_orderbook(self):
        '''
        returns all bids and ask values merged from all exchanges
        '''
        endpoint = "/merged-orderbook"
        return self._parent._send_request(endpoint)

    def whale_trades(self, exchange:str, coin:str):
        '''
        PREMIUM FEATURE
        returns executed large trades of one exchange


        exchange: Exchange Platform like "binance"

        coin: A Cryptocurrency. Example: BTC, XRP or XMR. Can also be found with market_list()
        '''
        endpoint = "/xtrades"
        args = self._parent._casefold(exchange=exchange, coin=coin)
        return self._parent._send_request(endpoint, args)

    def coin_info(self, exchange:str, filter:str):
        '''
        PREMIUM FEATURE
        returns all avaiable infos about a cryptocurrency


        exchange: Exchange Platform like "binance"

        filter: can be -> defi, pow, mineable, stablecoin, privacy, filesharing or all
        '''
        endpoint = "/cryptocurrency-info"
        args = self._parent._casefold(exchange=exchange, filter=filter)
        return self._parent._send_request(endpoint, args)

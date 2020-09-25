class _Liquidations():
        def __init__(self, parent):
            self._parent = parent
        
        def btc(self):
            '''
            returns "longs" and "shorts" for BTC
            '''
            endpoint = "/liquidation-data"
            return self._parent._send_request(endpoint)

        def bitmex(self, market_pair:str):
            '''
            returns Buy and Sell data with "market_pair", "quantity", "side" (SELL or BUY) and "timestamp"


            market_pair: Pair of Currencys. Each exchange has his own pairs. 
            You can find them by using market_list()
            '''
            endpoint = "/bitmex-liquidation"
            args = self._parent._casefold(market_pair=market_pair)
            return self._parent._send_request(endpoint, args)

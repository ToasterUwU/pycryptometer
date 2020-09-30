import json
import requests

from ._volumes import _Volumes
from ._infos import _Infos
from ._liquidations import _Liquidations
from ._indicators import _Indicators

class Cryptometer():
    def __init__(self, api_key):
        self._api_key = api_key
        self._api_url = "https://api.cryptometer.io"

        self.indicators = _Indicators(parent=self)
        self.infos = _Infos(parent=self)
        self.liquidations = _Liquidations(parent=self)
        self.volumes = _Volumes(parent=self)

    def _response(self, **args):
            no_data_errors = [
                "No Data",
                "No Liquidation"
            ]

            success = args["success"]
            error = args["error"]
            if "data" in args:
                data = args["data"]
            else:
                data = []

            if success == "true":
                success = True
            else:
                success = False

            if error == "false":
                error = None
            else:
                if args["error"] not in no_data_errors:
                    raise Exception(error)
                else:
                    success = True
            
            if success == True:
                return data

    def _casefold(self, exchange=None, market_pair=None, pair=None, coin=None, timeframe=None, exchange_type=None, source=None, period=None, long_period=None, short_period=None, signal_period=None):
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
        if long_period != None:
            args.update({"long_period": str(long_period)})
        if short_period != None:
            args.update({"short_period": str(short_period)})
        if signal_period != None:
            args.update({"signal_period": str(signal_period)})
        return args

    def _send_request(self, endpoint:str, arguments:dict={}):        
        args = ["api_key="+self._api_key]

        for x in arguments.items():
            args.append(x[0]+"="+x[1])

        url = self._api_url+endpoint+"?"+"&".join(args)
        r = requests.get(url)
        r = self._response(**json.loads(r.content.decode()))
        return self._fix_data(r)
    
    def _fix_data(self, r):
        if r != [] and type(r) == list: #list but not empty list
            if type(r[0]) == list: #first thing in it == list
                if len(r) == 1: #first thing == only thing
                    r = r[0]
            elif type(r[0]) == dict: #first thing in it == dict
                if len(r) == 1: #first thing == only thing
                    r = r[0]
        return r
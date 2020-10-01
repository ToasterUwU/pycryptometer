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
        '''
        This function is checking the output of the API and raises Exceptions if something goes wrong.
        '''
        no_data_errors = [ #Errors that dont raise a Execption
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
        '''
        This functions takes all arguments and normalizeses them, so the API accepts them.
        '''
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
        '''
        This function sends the API request and returns the json response as dict
        '''
        args = ["api_key="+self._api_key]

        for x in arguments.items():
            args.append(x[0]+"="+x[1]) #throwing the link arguments together

        url = self._api_url+endpoint+"?"+"&".join(args) #assembling the url
        r = requests.get(url) #sending the API request
        r = self._response(**json.loads(r.content.decode())) #sending data to _response for error checking
        return self._fix_data(r) #returning the data after sending it to _fix_data for fixing the topology
    
    def _fix_data(self, r):
        '''
        This function is fixing the formatting of the data
        '''
        if r != [] and type(r) == list: #list but not empty list
            if type(r[0]) == list or type(r[0]) == dict: #first thing in it == list or dict
                if len(r) == 1: #first thing == only thing
                    r = r[0]
        return r
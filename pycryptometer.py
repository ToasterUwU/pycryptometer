import requests
import json
class Cryptometer():
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.cryptometer.io"

    class Response():
        def __init__(self, **args):
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
                raise Exception(self.error)

    def _send_request(self, endpoint:str, arguments:dict):
        args = ["api_key="+self.api_key]

        for x in arguments.items():
            args.append(x[0]+"="+x[1])

        url = self.api_url+endpoint+"?"+"&".join(args)
        r = requests.get(url)
        return self.Response(**json.loads(r.content.decode()))

    def coinlist(self, exchange:str):
        endpoint = "/coinlist"
        exchange = exchange.lower()
        return self._send_request(endpoint, {"e": exchange})
    
    def tickerlist(self, exchange:str):
        endpoint = "/tickerlist"
        exchange = exchange.lower()
        return self._send_request(endpoint, {"e": exchange})
    
    def single_ticker(self, exchange:str, market_pair:str):
        endpoint = "/ticker"
        exchange = exchange.lower()
        market_pair = market_pair.replace("-", "").upper()
        return self._send_request(endpoint, {"e": exchange, "market_pair": market_pair})

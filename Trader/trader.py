"""
Asrın ÖZTİN - 2022 May
"""

"""
MIT License

Copyright (c) 2022 Asrın Öztin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""


"""
The USER is responsible for any purchase and sale transactions to be made via this python code.
The study does NOT guarantee success in any situation and does NOT accept any kind of responsibility for any matter.
All actions to be taken are in only and only responsibility of the USER, NOT the developer.

"""


"""
•	Root Functions*: Functions that directly and ONLY using Binance-Client module

•	Class IWalletEndPoints: Has ONLY Root Functions related to Binance-Client module/Wallet.

•	Class IMarketDataEndPoints: Has ONLY Root Functions related to Binance-Client module/MarketData.

•	Class ISpotAccountTradeEndPoints: Has ONLY Root Functions related to Binance_Client module/SpotAccountTrade.

•	Class IDerivedEndPoints: Has functions that are derived from the Root Functions.
        Such as changing the dataype of the returned value of the Root Function. The functions included are
            all can be tought as a bridge in between the Root Functions and the program itself.

•	Class IBinanceClientModuleBehaviors: Has functions that are used directly in the main Program.
        They differ from the functions in IDerivedEndPoints not by being dependent on the Root Functions but being
            directly used in the program. Basically, as an example, Root Functions get the data needed and IBinanceClientModuleBehaviors
                functions lets us use them in the program flow by using the IDerivedEndPoıints functions as a bridge.

•	Class IBinanceClientClassBehaviors: Has functions to maintain the main flow of the program.
        The functions included are all essential to use BinanceClient class itself and class instance objects.

•	Class Config holds the essential personal information required to construct BinanceClient.

•	Class BinanceClient: The key class of the whole program. It uses all other classes at some level.

•	Class Coin: The class to represent a basic Coin object’s attributes in real life. It also has the mission
        to notify the upTrendCoin and downTrendCoin classes’ symbol lists. Observer pattern is applied.

•	Class upTrendCoin: The class to store and get coins in up trend which are determined with the Strategy class whenever needed.
        It is continuously notified by the Coin class and is triggered in the main flow of the program.

•	Class downTrendCoin: The class to store and get coins in down trend which are determined with the Strategy class whenever needed.
        It is continuously notified by the Coin class and is triggered in the main flow of the program.

•	Class Indicator: The class is a premature class now. It will be useful if there will be lots of indicator types.

•	Class Sar: The class is a premature class for now. It will be useful if there will be lots of Sar indicator types.

•	Class Sar02_02: The class is a class with embed attributes and methods. The attributes that are used in the class are
        chosen with the studies based on algorithmic trading.

•	Class Wma: The class is a premature class for now. It will be useful if there will be lots of Wma indicator types.

•	Class Wma14: The class is a class with embed attributes and methods. The attributes that are used in the class are
        chosen with the studies based on algorithmic trading.

•	Class Macd: The class is a premature class for now. It will be useful if there will be lots of Macd indicator types

•	Class Macd26_12_9: The class is a class with embed attributes and methods. The attributes that are used in the class are
        chosen with the studies based on algorithmic trading.

•	Class Strategy: The class is a premature class now. It will be useful if there will be lots of Strategy types.

•	Class Strategy01: The class is a class with embed attributes and methods. The attributes that are used in the class are chosen with
        the data science studies based on algorithmic trading that are explained and tested in that very study.

"""

from abc import ABC, abstractmethod

from binance.client import Client
from binance.enums import *
from binance.helpers import round_step_size

import pandas as pd
import ta

import time

import json
import requests
import urllib

class IWalletEndPoints(ABC):
    @abstractmethod
    def get_asset_balance():
        # returns client.get_asset_balance(symbol)
        pass


class IMarketDataEndPoints(ABC):
    @abstractmethod
    def get_klines():
        # returns client.get_klines(symbol=symbol, interval=interval, limit=limit)
        pass

    @abstractmethod
    def get_symbol_ticker():
        # returns client.get_symbol_ticker(symbol=symbol)
        pass

    @abstractmethod
    def get_symbol_info():
        # returns client.get_symbol_info(symbol)
        pass

    @abstractmethod
    def get_exchange_info():
        # returns client.get_exchange_info()
        pass


class ISpotAccountTradeEndPoints(ABC):
    @abstractmethod
    def create_order():
        # if succeed returns client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity): dict() ; else if not succeed returns False: bool()
        pass

    @abstractmethod
    def get_account_info():
        # returns client.get_account()
        pass


class IDerivedEndPoints(ABC):
    # get_symbol_info() dependency
    @abstractmethod
    def get_symbol_info_filters():
        # returns self.get_symbol_info(symbol)["filters"]  where self is a BinanceClient Class Instance
        pass

    # get_symbol_info() dependency
    @abstractmethod
    def get_filters_lot_size():
        # returns filters = self.get_symbol_info_filters(symbol)[:][2]  where self is a BinanceClient Class Instance
        pass

    # get_symbol_info() dependency
    @abstractmethod
    def get_filters_min_notional():
        # returns filters = self.get_symbol_info_filters(symbol)[:][3]  where self is a BinanceClient Class Instance
        pass

    # get_account_info() dependency
    @abstractmethod
    def get_account_info_balances():
        # returns self.get_account_info()["balances"]  where self is a BinanceClient Class Instance
        pass

    # get_account_info() dependency
    @abstractmethod
    def get_assets():
        # returns assets which is [x["asset"] for x in balances[:]] where balances = self.get_account_info_balances() and  where self is a BinanceClient Class Instance
        pass


class IBinanceClientModuleBehaviors(ABC):
    # get_symbol_info() dependency
    @abstractmethod
    def get_symbol_min_quantity():
        # returns self.get_filters_lot_size(symbol)["minQty"] where self is a BinanceClient Class Instance
        pass

    # get_symbol_info() dependency
    @abstractmethod
    def get_symbol_step_size():
        # returns self.get_filters_lot_size(symbol)["stepSize"] where self is a BinanceClient Class Instance
        pass

    # get_symbol_info() dependency
    @abstractmethod
    def get_symbol_min_notional():
        # returns self.get_filters_min_notional(symbol)["minNotional"] where self is a BinanceClient Class Instance
        pass

    # get_asset_balance() dependency
    @abstractmethod
    def get_asset_balance_free():
        # returns float(asset_balance["free"]) where asset_balance = self.get_asset_balance(asset) wheere self is a BinanceClient Class Instance
        pass

    # get_account_info() dependency
    @abstractmethod
    def get_assets_owned():
        # returns [x["asset"] for x in balances[:] if float(x["free"]) > 0.0] where balances = self.get_account_info_balances() where self is a BinanceClient Class Instance
        pass

    # get_account_info() dependency
    @abstractmethod
    def is_asset_owned():
        # returns (symbol in owned_assets) where owned_assets = self.get_assets_owned() where self is a BinanceClient Class Instance
        pass

    @abstractmethod
    def is_asset_owned_enough():
        # returns True if asset is owned enough. It prevents errors while checking if an asset is owned. Otherwise the possible error occurs while trying to sell 0.xyz where 0.xyz <= step_size of the symbol
        pass

    # get_klines() dependency
    @abstractmethod
    def get_klines_properly():
        # returns each value returned by self.get_klines(symbol=symbol, interval=interval, limit=limit) as converting them as pd.Series([float(x[n]) for x in klines]) where self is a BinanceClient Class Instance
        pass

    # get_symbol_ticker() dependency
    @abstractmethod
    def get_symbol_ticker_price():
        # returns float(symbol_ticker_price) where symbol_ticker_price = self.get_symbol_ticker(symbol)["price"] where self is a BinanceClient Class Instance
        pass

    # get_exchange_info() dependency
    @abstractmethod
    def get_exchange_info_symbols():
        # returns self.get_exchange_info()["symbols"] where self is a BinanceClient Class Instance
        pass


class IBinanceClientClassBehaviors(ABC):
    @abstractmethod
    def calculate_quantity_to_buy():
        # calculates and returns the quantity to buy
        pass

    @abstractmethod
    def calculate_quantity_to_sell():
        # calculates and returns the quantity to sell
        pass

    @abstractmethod
    def get_total_wallet_wealth():
        # calculates and returns the total wallet wealth in quote asset units
        pass

    @abstractmethod
    def sell():
        # sells the symbol sent as param
        pass

    @abstractmethod
    def buy():
        # buys the symbol sent as param
        pass


class Config:
    def __init__(self, api_key: str, api_secret: str):
        self.__api_key = api_key
        self.__api_secret = api_secret    

    def get_api_key(self):
        return self.__api_key

    def get_api_secret(self):
        return self.__api_secret


class BinanceClient(IWalletEndPoints,
                    IMarketDataEndPoints,
                    ISpotAccountTradeEndPoints,
                    IDerivedEndPoints,
                    IBinanceClientModuleBehaviors,
                    IBinanceClientClassBehaviors):

    def __init__(self, quote_asset: str, target_asset_list: list, config: Config, testnet=False):        
        self.__api_key = config.get_api_key()
        self.__api_secret = config.get_api_secret()
        self.__tld = "com"
        self.__testnet = testnet
        self.client = Client(api_key=self.__api_key, api_secret=self.__api_secret,
                             tld=self.__tld, testnet=self.__testnet)

        self.__quote_asset = quote_asset
        self.__target_asset_list = target_asset_list

        Coin.arange_symbol_list(self)

    def get_quote_asset(self):
        return self.__quote_asset

    def get_target_asset_list(self):
        return self.__target_asset_list

    """
    IWalletEndpoints
    """

    def get_asset_balance(self, symbol: str):
        try:
            asset_balance = self.client.get_asset_balance(symbol)
            return asset_balance
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_asset_balance()".format(e))

    """
    IMarketDataEndPoints
    """

    def get_klines(self, symbol: str, interval, limit=500):
        try:
            klines = self.client.get_klines(
                symbol=symbol, interval=interval, limit=limit)
            return klines
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_klines()".format(e))

    def get_symbol_ticker(self, symbol: str):
        try:
            symbol_ticker = self.client.get_symbol_ticker(symbol=symbol)
            return symbol_ticker
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_symbol_ticker()".format(e))

    def get_symbol_info(self, symbol: str):
        try:
            symbol_info = self.client.get_symbol_info(symbol)
            return symbol_info
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_symbol_info()".format(e))

    def get_exchange_info(self):
        try:
            exchange_info = self.client.get_exchange_info()
            return exchange_info
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_exchange_info()".format(e))

    """
    ISpotAccountTradeEndpoints
    """

    def create_order(self, symbol: str, side, quantity: float, order_type=FUTURE_ORDER_TYPE_MARKET):
        try:
            order = self.client.create_order(
                symbol=symbol, side=side, type=order_type, quantity=quantity)
            return order
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/create_order()".format(e))
            return False

    def get_account_info(self):
        try:
            account = self.client.get_account()
            return account
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_account_info()".format(e))

    """
    IDerivedEndPoints
    """

    def get_symbol_info_filters(self, symbol: str):
        try:
            symbol_info = self.get_symbol_info(symbol)
            filters = symbol_info["filters"]
            return filters
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_symbol_info_filters()".format(e))

    def get_filters_lot_size(self, symbol: str):
        try:
            filters = self.get_symbol_info_filters(symbol)
            lot_size = filters[:][2]
            return lot_size
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_filters_lot_size()".format(e))

    def get_filters_min_notional(self, symbol: str):
        try:
            filters = self.get_symbol_info_filters(symbol)
            min_notional = filters[:][3]
            return min_notional
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_filters_min_notional()".format(e))

    def get_account_info_balances(self):
        try:
            account = self.get_account_info()
            balances = account["balances"]
            return balances
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_account_info_balances()".format(e))

    def get_assets(self):
        try:
            balances = self.get_account_info_balances()
            assets = [x["asset"] for x in balances[:]]
            return assets
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_assets()".format(e))

    """
    IBinanceClientModuleBehaviors
    """

    def get_symbol_min_quantity(self, symbol: str):
        try:
            lot_size = self.get_filters_lot_size(symbol)
            min_quantity = lot_size["minQty"]
            return min_quantity
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_symbol_min_quantity()".format(e))

    def get_symbol_step_size(self, symbol: str):
        try:
            lot_size = self.get_filters_lot_size(symbol)
            step_size = lot_size["stepSize"]
            return float(step_size)
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_symbol_step_size()".format(e))

    def get_symbol_min_notional(self, symbol: str):
        try:
            min_notional = self.get_filters_min_notional(symbol)
            min_notional = min_notional["minNotional"]
            return float(min_notional)
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_symbol_min_notional()".format(e))

    def get_asset_balance_free(self, asset: str):
        try:
            asset_balance = self.get_asset_balance(asset)
            free_asset = float(asset_balance["free"])
            return free_asset
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_asset_balance_free()".format(e))

    def get_assets_owned(self):
        try:
            balances = self.get_account_info_balances()
            assets = [x["asset"]
                      for x in balances[:] if float(x["free"]) > 0.0]
            return assets
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_assets_owned()".format(e))

    def get_assets_owned_enough(self):
        try:
            quote_asset = self.get_quote_asset()
            owned_assets = self.get_assets_owned()
            owned_assets_except_quote_asset = [
                x for x in owned_assets if x != quote_asset]

            assets_owned_enough = [
                x for x in owned_assets_except_quote_asset if self.is_asset_owned_enough(x) == True]
            return assets_owned_enough
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_assets_owned_enough()".format(e))

    def is_asset_owned(self, asset: str):
        try:
            owned_assets = self.get_assets_owned()
            return (asset in owned_assets)
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/is_asset_owned()".format(e))

    def is_asset_owned_enough(self, asset: str):
        try:
            quote_asset = self.get_quote_asset()
            symbol = asset + quote_asset

            step_size = self.get_symbol_step_size(symbol)
            min_notional = self.get_symbol_min_notional(symbol)
            curr_price = self.get_symbol_ticker_price(symbol)
            owned_quantity = self.get_asset_balance_free(asset)
            owned_value = curr_price * owned_quantity

            return ((owned_quantity > step_size) and (owned_value > min_notional))
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/is_asset_owned_enough()".format(e))

    def get_klines_properly(self, symbol: str, interval, limit=500):
        try:
            klines = self.get_klines(
                symbol=symbol, interval=interval, limit=limit)

            opens = pd.Series([float(x[1]) for x in klines])
            highs = pd.Series([float(x[2]) for x in klines])
            lows = pd.Series([float(x[3]) for x in klines])
            closes = pd.Series([float(x[4]) for x in klines])
            volumes = pd.Series([float(x[5]) for x in klines])

            return opens, highs, lows, closes, volumes

        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_klines_properly()".format(e))

    def get_symbol_ticker_price(self, symbol: str):
        try:
            symbol_ticker_price = self.get_symbol_ticker(symbol)[
                "price"]
            return float(symbol_ticker_price)
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_symbol_ticker_price()".format(e))

    def get_exchange_info_symbols(self):
        try:
            symbols = self.get_exchange_info()["symbols"]
            return symbols
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_exchange_info_symbols()".format(e))

    """
    BinanceClientClassBehaviors
    """

    def calculate_quantity_to_buy(self, symbol: str):
        try:
            quote_asset = self.get_quote_asset()
            if self.is_asset_owned(quote_asset):
                curr_lot_price = self.get_symbol_ticker_price(symbol)
                asset_balance_free = self.get_asset_balance_free(quote_asset)
                total_coin_count = len(Coin.get_symbol_list())
                avg = asset_balance_free / total_coin_count

                step_size = float(self.get_symbol_step_size(symbol))                

                quantity_to_buy = avg / curr_lot_price
                final_quantity_to_buy = round_step_size(
                    quantity_to_buy, step_size)                                             

                return final_quantity_to_buy
            
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/calculate_quantity_to_buy()".format(e))

    def calculate_quantity_to_sell(self, symbol: str):
        try:
            quote_asset = self.get_quote_asset()
            asset = symbol[:-len(quote_asset)]

            quantity_to_sell = float(self.get_asset_balance_free(asset))
            step_size = float(self.get_symbol_step_size(symbol))
                        
            final_quantity_to_sell = round_step_size(
                quantity_to_sell, step_size)

            return final_quantity_to_sell
        
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/calculate_quantity_to_sell()".format(e))

    def get_total_wallet_wealth(self):
        try:
            quote_asset = self.get_quote_asset()
            owned_assets = self.get_assets_owned()
            owned_assets_except_quote_asset = [
                x for x in owned_assets if x != quote_asset]
            available_symbols = Coin.get_symbol_list()

            asset_balances_free = [float(self.get_asset_balance_free(str(
                x))) for x in owned_assets_except_quote_asset if str(x) + str(quote_asset) in available_symbols]

            asset_current_ticker_prices = [float(self.get_symbol_ticker_price(str(
                x) + str(quote_asset))) for x in owned_assets_except_quote_asset if str(x) + str(quote_asset) in available_symbols]

            curr_wealth_list = [
                float(x*y) for x, y in zip(asset_balances_free, asset_current_ticker_prices)]

            curr_wealth = sum(curr_wealth_list) + \
                float(self.get_asset_balance_free(quote_asset))

            return float(round(curr_wealth, 2))
            
        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/get_total_wallet_wealth()".format(e))

    def sell(self, asset: str):
        try:
            symbol = asset + self.get_quote_asset()
            quantity_to_sell = self.calculate_quantity_to_sell(symbol)
            print(quantity_to_sell)

            order = self.create_order(symbol, SIDE_SELL, quantity_to_sell)

            if order is not False:
                executed_quantity = order["executedQty"]
                text = "I just sold {} x {}.".format(executed_quantity, asset) + "\nCurrent total wallet wealth (in quote asset): {} \nTime: {}".format(
                    str(self.get_total_wallet_wealth()), str(time.asctime(time.localtime())))                
                print(text)

        except Exception as e:
            print(
                "An exception occured: {0} at BinanceClient/sell()".format(e))

    def buy(self, asset: str):
        try:
            symbol = asset + self.get_quote_asset()
            quantity_to_buy = self.calculate_quantity_to_buy(symbol)
            print(quantity_to_buy)

            order = self.create_order(symbol, SIDE_BUY, quantity_to_buy)
            if order is not False:
                executed_quantity = order["executedQty"]
                text = "I just bought {} x {}.".format(executed_quantity, asset) + "\nCurrent total wallet wealth (in quote asset): {} \nTime: {}".format(
                    str(self.get_total_wallet_wealth()), str(time.asctime(time.localtime())))
                print(text)

        except Exception as e:
            print("An exception occured: {0} at BinanceClient/buy()".format(e))


class Coin:
    __symbol_list = []

    @classmethod
    def arange_symbol_list(cls, client: BinanceClient):
        try:
            available_symbols_list = list(cls.eliminate_symbols(
                cls, client, symbols_dict=cls.load_symbols(client)).keys())

            cls.__symbol_list = [str(str(x) + client.get_quote_asset()) for x in client.get_target_asset_list() if str(
                str(x) + client.get_quote_asset()) in available_symbols_list]                        
        except Exception as e:
            print(
                "An exception occured: {0} at Coin/arange_symbol_list()".format(e))

    @staticmethod
    def eliminate_symbols(cls, client: BinanceClient, symbols_dict: dict):
        try:
            available_symbols_dict = {outer_k:
                                      {inner_k: inner_v for inner_k,
                                       inner_v in outer_v.items()}
                                      for outer_k, outer_v in symbols_dict.items()
                                      if outer_v["quoteAsset"] == client.get_quote_asset() and outer_v["isSpotTradingAllowed"] == True}

            return available_symbols_dict
        except Exception as e:
            print(
                "An exception occured: {0} at Coin/eliminate_symbols()".format(e))

    @classmethod
    def load_symbols(cls, client: BinanceClient):
        try:
            symbols_dict = dict()
            symbols = client.get_exchange_info_symbols()

            for curr_symbol in symbols:
                symbol_name = curr_symbol["symbol"]
                symbol_base_asset = curr_symbol["baseAsset"]
                symbol_quote_asset = curr_symbol["quoteAsset"]
                symbol_is_spot_trading_allowed = curr_symbol["isSpotTradingAllowed"]

                symbols_dict[symbol_name] = {"baseAsset": symbol_base_asset,
                                             "quoteAsset": symbol_quote_asset,
                                             "isSpotTradingAllowed": symbol_is_spot_trading_allowed}
            return symbols_dict
        except Exception as e:
            print("An exception occured: {0} at Coin/load_symbols()".format(e))

    @classmethod
    def notify_observers(cls, client: BinanceClient):
        try:
            upTrendCoin.update_symbol_list(client)
            downTrendCoin.update_symbol_list(client)
        except Exception as e:
            print(
                "An exception occured: {0} at Coin/notify_observers()".format(e))

    @classmethod
    def get_symbol_list(cls):
        return cls.__symbol_list


class upTrendCoin:
    __symbol_list = []

    @classmethod
    def update_symbol_list(cls, client: BinanceClient):
        try:
            cls.__symbol_list = [x for x in Coin.get_symbol_list() if Strategy01.eliminator(
                client, str(x)) == "1"]
        except Exception as e:
            print(
                "An exception occured: {0} at upTrendCoin/update_symbol_list()".format(e))

    @classmethod
    def get_symbol_list(cls):
        return cls.__symbol_list


class downTrendCoin:
    __symbol_list = []

    @classmethod
    def update_symbol_list(cls, client: BinanceClient):
        try:
            coin_symbol_list = Coin.get_symbol_list()
            upTrendCoin_symbol_list = upTrendCoin.get_symbol_list()

            cls.__symbol_list = [
                x for x in coin_symbol_list if x not in upTrendCoin_symbol_list]
        except Exception as e:
            print(
                "An exception occured: {0} at downTrendCoin/update_symbol_list()".format(e))

    @classmethod
    def get_symbol_list(cls):
        return cls.__symbol_list


class Indicator:
    @classmethod
    def calculate_indicator():
        pass

class Macd(Indicator):
    @classmethod
    def calculate_indicator(cls, closes, window_slow, window_fast, window_sign):
        return pd.Series(ta.trend.MACD(closes, window_slow = window_slow, window_fast = window_fast, window_sign = window_sign).macd_diff(), dtype = float)

class Macd26_12_9(Macd):
    WINDOW_SLOW = 26
    WINDOW_FAST = 12
    WINDOW_SIGN = 9
    
    @classmethod
    def calculate_indicator(cls, closes, window_slow=WINDOW_SLOW, window_fast = WINDOW_FAST, window_sign = WINDOW_SIGN):
        try:
            return pd.Series(ta.trend.MACD(closes, window_slow = window_slow, window_fast = window_fast, window_sign = window_sign).macd_diff(), dtype = float)
        except Exception as e:
            print(
                "An exception occured: {0} at Macd26_12_9/calculate_indicator()".format(e))

class Sar(Indicator):
    @classmethod
    def calculate_indicator(cls, highs, lows, closes, step, max_step):
        return pd.Series(ta.trend.PSARIndicator(highs, lows, closes, step, max_step).psar(), dtype=float)


class Sar02_02(Sar):
    STEP = 0.2
    MAX_STEP = 0.2

    @classmethod
    def calculate_indicator(cls, highs, lows, closes, step=STEP, max_step=MAX_STEP):
        try:
            return pd.Series(ta.trend.PSARIndicator(highs, lows, closes, step=step, max_step=max_step).psar(), dtype=float)
        except Exception as e:
            print(
                "An exception occured: {0} at Sar02_02/calculate_indicator()".format(e))


class Wma(Indicator):
    @classmethod
    def calculate_indicator(cls, closes, window):
        return pd.Series(ta.trend.WMAIndicator(closes, window = window).wma(), dtype = float)
          

class Wma14(Wma):
    WINDOW = 14

    @classmethod
    def calculate_indicator(cls, closes, window=WINDOW):
        try:
            return pd.Series(ta.trend.WMAIndicator(closes, window = window).wma(), dtype = float)
        except Exception as e:
            print(
                "An exception occured: {0} at Wma14/calculate_indicator()".format(e))


class Strategy:
    @classmethod
    def determinator(cls, client, symbol):
        pass

    @classmethod
    def eliminator(cls, client: BinanceClient, symbol):
        pass


class Strategy01(Strategy):
    @classmethod
    def determinator(cls, client: BinanceClient, symbol: str):
        try:
            opens, highs, lows, closes, volumes = client.get_klines_properly(
                symbol, KLINE_INTERVAL_15MINUTE, None)

            ha_opens, ha_highs, ha_lows, ha_closes, ha_volumes = cls.heiken_ashi(
                opens, highs, lows, closes, volumes)
            curr_ha_close = ha_closes.iloc[-1]

            if cls.is_macd_positive(closes):
                to_ret = "1"
            else:
                to_ret = "0"

            return to_ret
        except Exception as e:
            print(
                "An exception occured: {0} at Strategy01/determinator()".format(e))

    @classmethod
    def eliminator(cls, client: BinanceClient, symbol: str):
        try:
            opens, highs, lows, closes, volumes = client.get_klines_properly(
                symbol, KLINE_INTERVAL_1HOUR, None)

            ha_opens, ha_highs, ha_lows, ha_closes, ha_volumes = cls.heiken_ashi(
                opens, highs, lows, closes, volumes)
            curr_ha_close = ha_closes.iloc[-1]

            if cls.is_up_trend(highs, lows, closes, curr_ha_close):
                to_ret = "1"
            else:
                to_ret = "0"

            return to_ret
        except Exception as e:
            print(
                "An exception occured: {0} at Strategy01/eliminator()".format(e))

    @classmethod
    def is_up_trend(cls, highs, lows, closes, curr_ha_close):
        try:
            if cls.is_wma_below(closes, curr_ha_close):
                if cls.is_sar_below(highs, lows, closes, curr_ha_close):
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(
                "An exception occured: {0} at Strategy01/is_up_trend()".format(e))

    @staticmethod
    def is_sar_below(highs, lows, closes, curr_ha_close):
        try:
            sar_result = Sar02_02.calculate_indicator(highs, lows, closes)
            curr_sar = sar_result.iloc[-1]                        

            return curr_sar < curr_ha_close
        except Exception as e:
            print(
                "An exception occured: {0} at Strategy01/is_sar_below()".format(e))

    @staticmethod
    def is_macd_positive(closes):
        try:
            macd_result = Macd26_12_9.calculate_indicator(closes)
            curr_macd = macd_result.iloc[-1]

            return curr_macd > 0
        except Exception as e:
            print(
                "An exception occured: {0} at Strategy01/is_macd_positive()".format(e))


    @staticmethod
    def is_wma_below(closes, curr_ha_close):
        try:
            wma_result = Wma14.calculate_indicator(closes)
            curr_wma = wma_result.iloc[-1]

            return curr_wma < curr_ha_close
        except Exception as e:
            print(
                "An exception occured: {0} at Strategy01/is_wma_below()".format(e))

    @staticmethod
    def heiken_ashi(opens, highs, lows, closes, volumes):
        try:
            ha_closes = pd.Series([], dtype=float)
            ha_opens = pd.Series([], dtype=float)
            ha_highs = pd.Series([], dtype=float)
            ha_lows = pd.Series([], dtype=float)
            ha_volumes = pd.Series([], dtype=float)

            for i in range(0, len(closes)):
                ha_closes[i] = (opens[i] + highs[i] + lows[i] + closes[i]) / 4
                if i == 0:
                    ha_opens[i] = (opens[i] + closes[i]) / 2
                else:
                    ha_opens[i] = (opens[i - 1] + closes[i - 1]) / 2
                ha_highs[i] = max(opens[i], closes[i], highs[i])
                ha_lows[i] = min(opens[i], closes[i], lows[i])

            ha_volumes = volumes

            return ha_opens, ha_highs, ha_lows, ha_closes, ha_volumes
        except Exception as e:
            print(
                "An exception occured: {0} at Strategy01/heiken_ashi()".format(e))


def flow(main_client: BinanceClient):
    Coin.notify_observers(main_client)
    print("Observers are notified")
    print("Current Rises in main trend: ", upTrendCoin.get_symbol_list())
    print("Current Falls in main trend: ", downTrendCoin.get_symbol_list())

    if len(upTrendCoin.get_symbol_list()) == 0:
        if len(main_client.get_assets_owned()) <= 1:
            return

    for curr_symbol in upTrendCoin.get_symbol_list():
        curr_asset = curr_symbol[:-len(main_client.get_quote_asset())]
        print("Current asset: ", curr_asset)
        if main_client.is_asset_owned_enough(curr_asset):
            print("I own: ", curr_asset)
            if Strategy01.determinator(main_client, curr_symbol) == "0":
                print("Fall started in minor trend. Selling: ", curr_symbol)
                main_client.sell(curr_asset)
            else:
                print("The rise continues in minor trend. I hold the position: ", curr_symbol)
        else:
            print("I do not own:", curr_asset)
            if Strategy01.determinator(main_client, curr_symbol) == "1":
                print("Rise started in minor trend. Buying: ", curr_symbol)
                main_client.buy(curr_asset)
            else:
                print("The fall continues in minor trend. I hold the position: ", curr_symbol)

    for curr_symbol in downTrendCoin.get_symbol_list():
        curr_asset = curr_symbol[:-len(main_client.get_quote_asset())]
        if main_client.is_asset_owned_enough(curr_asset):
            print("I own: ", curr_asset)
            print("Fall started in the main trend. Selling:  ", curr_symbol)
            main_client.sell(curr_asset)
        else:
            print("I do not own:", curr_asset)
            print("The fall continues in the main trend. I hold the position: ", curr_symbol)

    text = "Current wealth: {} \nTime: {}".format(
        str(main_client.get_total_wallet_wealth()), str(time.asctime(time.localtime())))
    print(text)
    


def main():
    config = Config(api_key="",
                    api_secret="")
    
    target_asset_list = ["BTC", "BNB"]
    
    quote_asset = "USDT"

    main_client = BinanceClient(
        quote_asset=quote_asset, target_asset_list=target_asset_list, config=config)
    

    while True:
        try:
            flow(main_client)
            time.sleep(300)
        except Exception as e:
            print("An exception occured: {0}".format(e))


if __name__ == '__main__':
    main()

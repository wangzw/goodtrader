# -*- coding: utf8 -*-

import tushare as ts
from sqlalchemy import create_engine
from ..common.configure import DB_CONNECT_STRING

engine = create_engine(DB_CONNECT_STRING)
df = ts.get_h_data('002337',autype=None, with_factor=True)
df.to_sql('002337', engine)


class Company(object):
    '''Company basic information
    '''

    def __init__(self, name, stock_id):
        self.name = name
        self.stock_id = stock_id

    def __str__(self):
        return self.name + " (" + self.stock_id + ")"


class Stock(object):

    def __init__(self, open=0, close=0, high=0, low=0, volume=0, amount=0):
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume
        self.amount = amount

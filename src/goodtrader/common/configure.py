# -*- coding:utf-8 -*-
'''
Setting configure parameters
'''

import yaml
from os.path import expanduser, isfile, sep

CONFIG_PATH = expanduser("~") + sep + ".trading_conf.yaml"

DB_CONNECT_STRING = "postgresql+psycopg2://localhost/trading"


def _load_config(stream):
    config = yaml.safe_load(stream)
    if config and "DB_CONNECT_STRING" in config:
        global DB_CONNECT_STRING
        DB_CONNECT_STRING = config["DB_CONNECT_STRING"]
        print(DB_CONNECT_STRING)

if isfile(CONFIG_PATH):
    _load_config(open(CONFIG_PATH))

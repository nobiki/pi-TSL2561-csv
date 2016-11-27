#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.dirname(__file__)+"/../")
from TSL2561Logger import *
logger = TSL2561Logger()

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])

    lux = logger.getLux()

    yield str(lux).encode('utf-8')

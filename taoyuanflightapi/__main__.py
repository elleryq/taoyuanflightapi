#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)


from taoyuanflightapi import get_current_flights

print(get_current_flights())

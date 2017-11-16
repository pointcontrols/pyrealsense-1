# -*- coding: utf-8 -*-
# Licensed under the Apache-2.0 License, see LICENSE for details.

"""This module extract the RS_API_VERSION to which pyrealsense is binded and wraps several enums 
from rs.h into classes with the same name."""

import pycparser
import io
import pickle

# Platform dependent
import os

import sys
from os import environ, path




loaded_globals = {}
loaded_classes = {}
try:
    with io.open(os.path.join(os.path.dirname(__file__), 'lrs_globals'), "rb") as ser_globals:
        loaded_globals= pickle.load(ser_globals)
        for name, val in loaded_globals.items():
            globals()[name] = val
except IOError:
    raise
try:
    with io.open(os.path.join(os.path.dirname(__file__), 'lrs_parsed_classes'), "rb") as ser2_classes:
        loaded_classes = pickle.load(ser2_classes)
        for class_name, class_dict in loaded_classes.items():
            class_gen = type(class_name, (object,), class_dict)
            #print("class dict:", class_dict);
            globals()[class_name] = class_gen
except IOError:
    raise


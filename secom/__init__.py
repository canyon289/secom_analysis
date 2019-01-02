"""Exploratory Package for SECOM Dataset."""
__version__ = "0.0.1"

import os
import logging


# Configure logging before importing arviz internals
_log = logging.getLogger("seconm")

if not logging.root.handlers:
    handler = logging.StreamHandler()
    _log.setLevel(logging.INFO)
    _log.addHandler(handler)


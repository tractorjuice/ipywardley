"""Wardley Map magic"""
__version__ = '0.0.2'

from .wardley import WardleyMagics

def load_ipython_extension(ipython):
    ipython.register_magics(WardleyMagics)
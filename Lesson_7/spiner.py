"""Spiner"""

import time

symbols = ["\\", "|", "/", "--"]

while True:
    for symbol in symbols:
        print(f"\r{symbol}", end="")
        time.sleep(0.5)

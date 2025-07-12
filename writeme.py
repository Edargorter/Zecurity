#!/usr/bin/env python3

import time
import os
import sys

class Writeme:

    def __init__(self, filename, rate):
        self.filename = filename
        self.rate = rate
        self.lines = []

    def read_file(self):
        with open(self.filename, 'r') as f:
            self.lines = [l.rstrip('\n') for l in f.readlines()]

    def print_file(self):
        if sys.platform.startswith('win'):
            os.system("cls")
        else:
            os.system("clear")
        for line in self.lines:
            for c in line:
                print(c, end="", flush=True)
                if c in [" ", "\t"]:
                    time.sleep(self.rate/2)
                else:
                    time.sleep(self.rate)
            print("\r\n", end="")

if __name__ == "__main__":
    filename = "writeme.py"
    rate = 0.05
    wm = Writeme(filename, rate)
    wm.read_file()
    wm.print_file()

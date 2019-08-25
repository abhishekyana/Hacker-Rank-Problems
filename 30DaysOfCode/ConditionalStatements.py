#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    text = ""
    if N%2==1:
        text = "Weird"
    if N%2==0:
        if N in list(range(2, 6)):
            text = "Not Weird"
        if N in list(range(6, 21)):
            text = "Weird"
        if N>20:
            text = "Not Weird"
    print(text)

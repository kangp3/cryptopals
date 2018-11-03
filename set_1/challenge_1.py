#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse


HEX_DIGITS = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "a", "b", "c", "d", "e", "f",
]

B64_DIGITS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "+", "/",
]



def hex_to_int(s):
    val = 0
    for dig in s:
        val *= 16
        if dig.isdigit():
            val += int(dig)
        else:
            dig = dig.lower()
            val += ord(dig) - ord("a") + 10
    return val


def int_to_b64(i):
    if i == 0:
        return B64_DIGITS[0]

    b64 = ""
    while i > 0:
        dig = i % 64
        b64 = B64_DIGITS[dig] + b64
        i = i // 64
    return b64


def hex_to_b64(s):
    return int_to_b64(hex_to_int(s))


def main(hexstr):
    print(hex_to_b64(hexstr))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("hexstr")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))

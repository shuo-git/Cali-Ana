# coding=utf-8
# Copyright 2017-2020 The THUMT Authors

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import regex as re


PUNC_EXP = re.compile("[\p{P}]")
FULL = "　，．：；？！゛´｀＾＿—‐／＼〜｜‘’“”（）〔〕［］｛｝〈〉＋−＝＜＞′″¥＄％＃＆＊＠０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
HALF = "\x20\x2c\x2e\x3a\x3b\x3f\x21\x22\x27\x60\x5e\x5f\x2d\x2d\x2f\x5c\x7e\x7c\x27\x27\x22\x22\x28\x29\x5b\x5d\x5b\x5d\x7b\x7d\x3c\x3e\x2b\x2d\x3d\x3c\x3e\x27\x22\x5c\x24\x25\x23\x26\x2a\x40\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a"
TRANS = str.maketrans(FULL, HALF)


def z2h(s):
    return s.translate(TRANS)


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def is_punc(s):
    if re.search(PUNC_EXP, s):
        return True
    return False


def truecase(s):
    chars = list(s)

    for i in range(len(chars)):
        c = chars[i]

        if ord(c) < 128 and c.isalpha():
            chars[i] = c.lower()
            break

    return "".join(chars)


def detruecase(s):
    chars = list(s)

    for i in range(len(chars)):
        c = chars[i]

        if ord(c) < 128 and c.isalpha():
            chars[i] = c.upper()
            break

    return "".join(chars)


def deseg(s):
    chars = list(s.strip())
    outputs = []
    n = len(chars)

    for i in range(n):
        c = chars[i]

        if c == " ":
            if i == 0:
                continue
            elif n == i - 1:
                continue
            elif ord(chars[i-1]) >= 128 or ord(chars[i+1]) >= 128:
                continue
            elif is_punc(chars[i-1]) or is_punc(chars[i+1]):
                continue

        outputs.append(c)

    return "".join(outputs)


def restore_punc(s):
    chars = list(s.strip())
    outputs = []
    open_flag = True

    for i in range(len(chars)):
        c = chars[i]

        #if len(outputs) > 1 and ord(outputs[-1]) < 128:
        #    if i < len(chars) - 1 and ord(chars[i+1]) < 128:
        #        outputs.append(c)
        #        continue

        if c == "!":
            outputs.append("！")
        elif c == "(":
            outputs.append("（")
        elif c == ")":
            outputs.append("）")
        elif c == "\"":
            if open_flag:
                open_flag = False
                outputs.append("“")
            else:
                open_flag = True
                outputs.append("”")
        elif c == ",":
            outputs.append("，")
        elif c == ".":
            outputs.append("。")
        elif c == ":":
            outputs.append("：")
        elif c == ";":
            outputs.append("；")
        elif c == "?":
            outputs.append("？")
        elif c == "[":
            outputs.append("［")
        elif c == "]":
            outputs.append("］")
        elif c == "~":
            outputs.append("～")
        else:
            outputs.append(c)

    return "".join(outputs)


if __name__ == "__main__":
    for line in sys.stdin:
        line = deseg(line)
        line = restore_punc(line)
        line = line.replace("。。。。。。", "......")
        line = re.sub(r"(\d+)，(\d+)", r"\1,\2", line)
        line = re.sub(r"(\d+)。(\d+)", r"\1.\2", line)
        line = re.sub(r"([A-Za-z]+)。([A-Za-z]+)", r"\1.\2", line)
        line = re.sub(r"([A-Za-z])。）", r"\1.）", line)
        line = re.sub(r"（[a-zA-Z ]{3,}）", "", line)
        line = re.sub(r"(\d)。", r"\1.", line)
        line = re.sub(r"(.*)\.$", r"\1。", line)
        #line = re.sub(r"[a-zA-Z ]+", "", line)

        sys.stdout.write(line.strip() + "\n")


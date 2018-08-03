#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    e = s.strip().split(' ')
    e = ''.join(e)
    l = math.sqrt(len(e))
    r = math.ceil(l)
    semi_encrypted = []
    while e:
        semi_encrypted.append(e[:r])
        e = e[r:]
    encrypted_word = []
    encrypted_message = ' '
    for i in range(r):
        for s in semi_encrypted:
            try:
                encrypted_word.append(s[i])
            except:
                pass
        encrypted_word.append(' ')
        encrypted_message += ''.join(encrypted_word)
        encrypted_word = []

    return encrypted_message.strip()



if __name__ == '__main__':
    s = "if man was meant to stay on the ground god would have given us roots"
    result = encryption(s)
    print(result)

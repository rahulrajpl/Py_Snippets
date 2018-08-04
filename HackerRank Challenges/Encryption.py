#!/bin/python3

from math import ceil, sqrt

# Complete the encryption function below.
def encryption(s):
    # e = s.strip().split(' ')
    # e = ''.join(e)
    # l = math.sqrt(len(e))
    # r = math.ceil(l)
    # semi_encrypted = []
    # while e:
    #     semi_encrypted.append(e[:r])
    #     e = e[r:]
    # encrypted_word = []
    # encrypted_message = ' '
    # for i in range(r):
    #     for s in semi_encrypted:
    #         try:
    #             encrypted_word.append(s[i])
    #         except:
    #             pass
    #     encrypted_word.append(' ')
    #     encrypted_message += ''.join(encrypted_word)
    #     encrypted_word = []
    #
    # return encrypted_message.strip()

    ###
    # Following is the short version of the above naive method
    ###

    s = ''.join(s)
    c = int(ceil(sqrt(len(s))))
    return ' '.join(map(lambda x: s[x::c], range(c)))




if __name__ == '__main__':
    s = "if man was meant to stay on the ground god would have given us roots"
    print(s)
    result = encryption(s.strip().split(' '))
    print(result)

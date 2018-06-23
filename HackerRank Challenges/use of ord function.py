'''
ord() function returns the ASCII value of the character
'''
def designerPdfViewer(h, word):
    max_h = 0
    l = len(word)
    for i in list(word):
        max_h = max(h[ord(i)-97], max_h)
    return max_h * l

if __name__ == '__main__':


    # h = list(map(int, input().rstrip().split()))
    h = list(map(int, "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5".rstrip().split()))

    # word = input()
    word = "abc"

    result = designerPdfViewer(h, word)

    print(result)

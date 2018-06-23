


def viralAdvertising(n):
    p = 5
    total_likes = 0
    for i in range(1, n+1):
        likes = p // 2
        total_likes += likes
        p = likes * 3
    return total_likes


if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)

    print(result)
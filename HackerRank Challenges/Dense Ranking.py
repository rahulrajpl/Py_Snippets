"""
DENSE RANKING(12234...)
-------------
If A ranks ahead of B and C (which compare equal) which are both ranked
ahead of D, then A gets ranking number 1 ("first"), B gets ranking number 2
("joint second"), C also gets ranking number 2 ("joint second") and D gets
ranking number 3 ("Third").

"""
import bisect

def climbingLeaderboard(scores, alice):
    alice_ranking = []
    scores = list(set(scores))
    scores.sort()
    s = len(scores)
    for alice_rank in alice:
        alice_ranking.append(s-bisect.bisect_right(scores, alice_rank)+1)
    # print(alice_ranking)
    return alice_ranking
    # return [(s-bisect.bisect_right(scores, i)+1) for i in alice]
if __name__ == '__main__':

    # scores_count = int(input())
    scores_count = 7
    # scores = list(map(int, input().rstrip().split()))
    scores = [100, 100, 50, 40, 40, 20, 10]
    # alice_count = int(input())
    alice_count = 4
    # alice = list(map(int, input().rstrip().split()))
    alice = [5, 25, 50, 120]
    result = climbingLeaderboard(scores, alice)

    for i in result:
        print(i)



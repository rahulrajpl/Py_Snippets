from datetime import datetime

ad, am, ay = map(int, input().strip().split(' '))
ed, em, ey = map(int, input().strip().split(' '))

actual = datetime(ay, am, ad)
expected = datetime(ey, em, ed)

if actual < expected:
    print(0)
elif (am, ay) == (em, ey):
    print(15 * (ad-ed))
elif ay == ey:
    print(500 * (am-em))
else:
    print(10000)


# if (ad, am, ay) <= (ed, em, ey):
#     print(0)
# elif (am, ay) == (em, ey):
#     print(15 * (ad-ed))
# elif ay == ey:
#     print(500 * (am-em))
# else:
#     print(10000)
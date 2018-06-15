"""

Sort first names for all those who have email ID with gmail.com
"""


    if emailID.__contains__("@gmail.com"):
        sorted_names.append(firstName)

sorted_names.sort()
for name in sorted_names:
    print(name)

# A One-liner implementation of above snippet is as follows
# But as per Zen of Python, readability matters. So not recommended

# print("\n".join(sorted([l.split()[0] for l in [input() for _ in range(int(input()))] if '@gmail.com' in l])))


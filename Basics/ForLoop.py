#
# exp = [23,25,27,43,37]
# Total = 0
# for expense in exp:
#     Total += expense

# print("Your Total Expense is: ", Total)

# for i in range(len(exp)):
#     print('Month: ', i+1, " and expense is", exp[i])

for i in range(6):
    if i % 2 == 0:
        continue
    else:
        print(i ** 2)
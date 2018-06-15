month =['January','February','March','April','May','June','July','August','September','October','November','December']

# A list with one ending for each number from 1 to 31
endings=['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']

Year = input(r"Year: ")
MonthIndex = int(input(r"Month(1-12): "))-1
DayIndex = int(input(r"Day(1-31): "))-1

#Remember to subtract 1 from month and day to get a correct index

print("Your date is: " + month[MonthIndex] + " " + str(DayIndex+1) + endings[DayIndex] + ", " + Year)

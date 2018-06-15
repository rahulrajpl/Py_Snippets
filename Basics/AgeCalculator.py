from datetime import datetime

BornYear = input("Enter your year of Birth: ")
print("Your age is: ", datetime.now().year - int(BornYear))
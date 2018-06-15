
# with open("time.py") as f:
#     for line in f:
#         print(line)
#
# f = open("MyFile.txt","w")
# f.write("I Love javascript")
# f.close()
#
# f = open("MyFile.txt","a")
# f.write("I Love Python")
# f.write("\nI Love c++")
# f.close()
#
# f = open("MyFile.txt",'r')
# i=1
# word_count = 0
# for line in f.readlines():
#     word_count = len(line.split(" "))
#     print("Word Count is: ", word_count, "Line #",i , " - ", line)
#     i += 1

new_file = open("MyNewFile.txt", 'w')
print(new_file)
print(new_file.write("Test document"))

print(new_file.closed)
new_file.close()

with open("MyNewFile.txt",'r') as f:
    print(f.read())
print(new_file.closed)
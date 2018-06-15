import sys


class Solution:
    # Write your code here
    stack = []
    queue = []

    queue_count = 0

    char = None
    i = None

    def pushCharacter(self, c):
        self.stack.append(c)

    def enqueueCharacter(self, c):
        self.queue.append(c)
        self.queue_count += 1

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        self.i = len(self.queue) - self.queue_count
        self.char = self.queue[self.i]
        self.queue_count -= 1
        self.queue.remove(self.char)
        return self.char



# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
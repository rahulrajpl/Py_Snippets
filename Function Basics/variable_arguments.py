# Default Argument Values
def ask_user(prompt, retries=4, reminder="Please Try Again"):
    while True:
        ok = input(prompt)
        if ok in ('yes','y','Y'):
            return True
        if ok in ('No','n','N'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)

if __name__ == '__main__':
    ask_user("Do you really want to quit(y/n)?", 2)
    ask_user("Do you really want to quit(y/n)?", 2, 'Really?')
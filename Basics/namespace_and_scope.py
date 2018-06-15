def scope_test():
    def do_local():
        spam = "Local Spam"

    def do_nonlocal():
        nonlocal spam
        spam = "non local spam"

    def do_global():
        global spam
        spam = "Global"

    spam = "Test Spam"
    do_local()
    print("Local Assignment:",spam)
    do_nonlocal()
    print("NonLocal Assignment:", spam)
    do_global()
    print("Global Assignment:", spam)

scope_test()
print("In Global Scope", spam)
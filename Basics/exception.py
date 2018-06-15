x = input("Enter First Number: ")
y = input("Enter second Number ")

try:
    print("While dividing these two number I get: ", x/int(y))
except Exception as e:
    print("Oops!: ", e)
    print("Type of Exept is: ", type(e))

except TypeError as e:



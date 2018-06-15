# In a function keyword arguments follow positional arguments
# kwargs is what we call


def formal_params(a, *b):  # Formal Params of form *params will return a tuple
    print(a)
    print(b)


formal_params(1,2,3,4,5)


def formal_params_with_kwargs(a, *b, **c): #Formal params of form **params return Dictionary
    print(a)
    print(b)
    for i in c:
        print(i,":",c[i])


formal_params_with_kwargs(1,2,3,4,5,name1='Rahul',name2='Reshmi',name3='Parvathy')
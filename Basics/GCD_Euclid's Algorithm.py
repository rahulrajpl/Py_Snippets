def gcd(a,b):
    """
    Return the greatest common diviser of a and b
    
    >>> gcd(10,5)
    5
    
    >>> gcd(14,21)
    7
    
    >>> gcd(9,0)
    9
    """
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
        
    
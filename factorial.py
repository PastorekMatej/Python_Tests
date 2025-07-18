#count factorial of a number 

def factorial(n : int) -> int:
    """ Function that counts factorial of a number 

    Factorial is a function that calculates all product 

    Args: 
        n (int): Argument of the function that is used for factorial calculation 
    Return:
        (int): Return the factorial of the function 
    """
    
    result = 1
    for i in range(1,n+1,1):
        result = result * i
    return result

if __name__ == "__main__": 
    print(factorial(5))

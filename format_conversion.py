#7. Write a Python code to convert a string to an integer

def conversion(s : str) -> int:
    """" Function conversion from string to integrer
    Args:
        s(str): string that will be converted 
    Return: 
        int: integer of the entry string
    """
    return int(float(s))

if __name__ == "__main__":
    print(conversion("345"))
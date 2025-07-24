# write a program to remove duplicate from a list 

def remove_duplicate(lst:list) ->set:
    """ Function removes ducplicates from a list 
    Args: 
    lst(list): analysed list 
    
    return
    (list): filtered list 
    """
    
    unique_list = set(lst)
    return unique_list

if __name__ == "__main__":

    list = ["Matej","Matej","Jozed","Brano","Dezo","Dezo"]
    print(remove_duplicate(list))





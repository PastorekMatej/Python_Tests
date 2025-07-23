#rewrite the code using Pythonic approach and write pytest unity test

def common_elements(list1:list,list2:list) ->list:
    """ Find common elements in list

        Function finds common elements in 2 lists 
    Args:
    list1 (list): 1. list
    list2 (list): 2. list

    Return:
    list
    """
    j = []
    return [i for i in list1 if i in list2]

if __name__ == "__main__":
        print(common_elements(["1",2,3,"4"],["1","4"]))
              

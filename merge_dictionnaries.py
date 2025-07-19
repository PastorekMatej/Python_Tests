




def merge_dictionnaries(dict1: dict, dict2: dict) -> dict:  
    """ Function to merge 2 dictionnaries
    Args
        dict1(dict):
        dict2(dict):
    Return
        (dict): return the merged dictionnary 
    """
    return dict1 | dict2

if __name__ == "__main__":

    d1 = {"student_id": "Matej", "test": {"test_1": "1234", "test_2":"01022025", "test_3": "How are you doing?" }}
    d2 = {"student_id": "Fero", "conversation": {"conversation_id": "1235", "date":"01032025", "message": "What are you doing?"}}
    print(d1)
    print(d2)
    print(merge_dictionnaries(d1,d2))


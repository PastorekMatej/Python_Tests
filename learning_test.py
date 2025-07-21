import pytest 
from format_conversion import conversion
from merge_dictionnaries import merge_dictionnaries

def test_conversion():
    assert conversion("345") == 345
    assert conversion("3.456") == 3

def test_merge_dictionnaries():
    dict1 = {"user_id" : "Matej", "conversation" : {"t1":"123"}, "life" : "is beautiful" }
    dict2 = {"user_id" : "Jozed", "conversation" : {"t1":"123"}, "what" : "is true"}
    assert merge_dictionnaries(dict1,dict2) ==  {"user_id" : "Jozed", "conversation": {"t1":"123"}, "life" : "is beautiful", "what" :"is true"}
    assert merge_dictionnaries(dict1,dict2) ==  {"user_id" : "Jozed", "conversation": {"t1":"123"}, "what" : "is true", "life" : "is beautiful"}
    assert merge_dictionnaries(dict1,dict2) ==  {"user_id" : "Matej", "conversation": {"t1":"123"}, "what" : "is true", "life" : "is beautiful"}



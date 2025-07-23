import pytest 
from format_conversion import conversion
from merge_dictionnaries import merge_dictionnaries
from common_elements import common_elements

def test_conversion():
    assert conversion("345") == 345
    assert conversion("3.456") == 3

def test_merge_dictionnaries():
    dict1 = {"user_id" : "Matej", "conversation" : {"t1":"123"}, "life" : "is beautiful" }
    dict2 = {"user_id" : "Jozed", "conversation" : {"t1":"123"}, "what" : "is true"}
    assert merge_dictionnaries(dict1,dict2) ==  {"user_id" : "Jozed", "conversation": {"t1":"123"}, "life" : "is beautiful", "what" :"is true"}
    assert merge_dictionnaries(dict1,dict2) ==  {"user_id" : "Jozed", "conversation": {"t1":"123"}, "what" : "is true", "life" : "is beautiful"}

def common_elements():
    l1 = ["student_id", "Matej", "test", "test_1","1234","test_2","01022025", "test_3","How are you doing?"]
    l2 = ["student_id", "Fero", "conversation", "conversation_id", "1235", "date","01032025", "message", "What are you doing?"]
    assert(l1,l2) == ["student_id"]

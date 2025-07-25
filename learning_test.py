import pytest 
from format_conversion import conversion
from merge_dictionnaries import merge_dictionnaries
from common_elements import common_elements
from remove_duplicate import remove_duplicate
from access_dictionnary import access_dictionnary_insurance
from access_dictionnary import access_dictionnary_country
from check_palidrome import check_palidrome
from longest_word import find_longest_word
import json

def test_conversion():
    assert conversion("345") == 345
    assert conversion("3.456") == 3

def test_merge_dictionnaries():
    dict1 = {"user_id" : "Matej", "conversation" : {"t1":"123"}, "life" : "is beautiful" }
    dict2 = {"user_id" : "Jozed", "conversation" : {"t1":"123"}, "what" : "is true"}
    assert merge_dictionnaries(dict1,dict2) ==  {"user_id" : "Jozed", "conversation": {"t1":"123"}, "life" : "is beautiful", "what" :"is true"}
    assert merge_dictionnaries(dict1,dict2) ==  {"user_id" : "Jozed", "conversation": {"t1":"123"}, "what" : "is true", "life" : "is beautiful"}

def test_common_elements():
    l1 = ["student_id", "Matej", "test", "test_1","1234","test_2","01022025", "test_3","How are you doing?"]
    l2 = ["student_id", "Fero", "conversation", "conversation_id", "1235", "date","01032025", "message", "What are you doing?"]
    #assert(l1,l2) == ["student_id"]

def test_remove_duplicate():
    lst = ["Matej","Matej","Jozed","Brano","Dezo","Dezo"]
    assert remove_duplicate(lst) == {'Matej','Jozed','Brano','Dezo'}



with open("insurance_file.json","r") as file:
    table = json.load(file)

def test_access_dictionnary():
    assert access_dictionnary_insurance("BMZ", table["insurance_table"]) == 9000
    assert access_dictionnary_country("Slovakia", table["insurance_table"]) == 5000 

def test_check_palidrome():
    assert check_palidrome("janoj") == True
    assert check_palidrome("hhhhh") == True
    assert check_palidrome("abcd") == False

def test_longest_word():
    assert find_longest_word("jajaj qsdqsd 7687686") == '7687686'
# Rewrite the code using pythonic approach and test it with a test file 
# Write the number os wovels

wovels = ("aeiou")
def count_wovels(expression): 
    return sum (1 for caracter in expression if caracter in wovels)

if __name__ == "__main__":
    print(count_wovels("eiaatp"))
    print ("Hello Word")

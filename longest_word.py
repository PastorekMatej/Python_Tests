# find the longest word in a sentence

def find_longest_word(sentence: str) -> str:
    sentence= sentence.split(' ')
    longest = 0
    for i in sentence:
        if len(i) > longest:
            word = i
    return word 



if __name__ == "__main__":
    
    word = find_longest_word("Hello I am RO ddddddddddddddddddddds")
    print(word)

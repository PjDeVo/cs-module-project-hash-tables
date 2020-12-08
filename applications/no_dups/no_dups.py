def no_dups(s):
    # Your code here

    #seperate the words
    # add them to a dictionary
    # if word is already in the dictionary, remove it from new variable
    # return new variable


    words = s.split()
    newSentence = {}
    for word in words:
        if word in newSentence:
            pass
        else:
            newSentence[word] = 1
    return " ".join(newSentence.keys())




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
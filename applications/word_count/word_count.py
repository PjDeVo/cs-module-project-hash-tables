def word_count(s):
    ignore = '":;,.-+=/\|[]{}()*^&'

    words = s.split()
    
    wordCount = {}

    for word in words:
        word = word.strip(ignore).lower()
        if not word:
            break
        if word in wordCount:
            wordCount[word] +=1
        else:
            wordCount[word]= 1
    return wordCount


        



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
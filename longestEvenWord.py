# find longest even word in a sentence
def longestEvenWord(sentence):

    words = sentence.split()
    longEvenWord = "00"
    wordCount = 0

    for word in words:
        if (len(word) % 2) == 0:
            if (wordCount < len(word)):
                longEvenWord = word
                wordCount = len(word)

    print(longEvenWord)

longestEvenWord("abcade testinga")

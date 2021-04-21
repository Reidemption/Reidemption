
def checkWord(word):
    letters = ['a','b','g','e','h','x','y']

    if len(word) > 8:
        return False
    b = letters[:]
    for i in word:
        if i in b:
            b.remove(i)
        else:
            return False
    letters = b
    return letters

print(checkWord('bag'))
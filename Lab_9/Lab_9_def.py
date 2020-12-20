from random import randint

def get_string():
    s = ''
    n = randint(10, 50)
    for i in range(n):
        l = randint(2, 10)
        for j in range(l):
            s += chr(randint(96, 122))
        s += ' '
    return s.rstrip(' ')


def rem_words(s, sym):
    punctuation_marks = [',', '.', '!', '\n', '\t', '-', '_', '^', '+', '=', "'", '|', '/', '\\', '''"''', '?', '<',
                         '>', ':', ';', ']', '[', '(', ')', '{', '}', '#', '&', '%', '$', '@', '*']
    s_new = ''
    for el in s.split(' '):
        a = (el[0].lower() == sym)
        b = (el[-1].lower() == sym)
        c = (len(el)>1 and el[-1] in punctuation_marks and el[-2].lower() == sym)
        d = (len(el)>1 and el[0] in punctuation_marks and el[1].lower() == sym)
        if a or b or c or d:
            continue
        s_new += el+' '
    return s_new.rstrip()

def GetFromFile(dir):
    handle = open(dir)
    s = ''
    for line in handle:
        s += line
    return s
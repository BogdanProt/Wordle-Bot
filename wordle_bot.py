import random
import time
from math import log2

f = open("cuvinte_wordle.txt", 'r')
out_txt = open("out.txt", 'a')

words = [word.strip() for word in f]

best_word = ''
max_entropy = 0
result = ''

def calculateEntropy(word):
    patterns = {}
    for elem in words:
        pattern = ''

        for i in range(5):
            if elem[i] == word[i]:
                pattern += '🟩'
            elif word[i] in elem:
                pattern += '🟨'
            else:
                pattern += '⬜'
        
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1
    
    entropy = 0
    for i in patterns:
        p = patterns[i] / len(words)  # probability
        entropy += p * log2(p)

    return -entropy

def findBestWord():
    global best_word, max_entropy

    max_entropy = 0
    best_word = ''

    for word in words:
        entropy = calculateEntropy(word)
        if entropy > max_entropy and len(words) > 1:
            best_word = word
            max_entropy = entropy
        
        elif len(words) == 1:
            best_word = words[0]

def checkWord(word, pattern):
    if len(pattern) < 5:
        return 0
    
    for i in range(5):
        if pattern[i] == '⬜':
            if best_word[i] in word:
                return 0
        elif pattern[i] == '🟨':
            if best_word[i] == word[i]:
                return 0
            if best_word[i] not in word:
                return 0
        elif pattern[i] == '🟩':
            if not best_word[i] == word[i]:
                return 0
    
    return 1

def removeWord():
    global words

    f = open('output.txt', encoding='utf-8')
    pattern = f.readline()
    copy = words.copy()

    for word in copy:
        if checkWord(word, pattern) == 0:
            words.remove(word)

def waitResult():
    global result
    output = open('output.txt', 'r+', encoding='utf-8')
    pattern = output.read()
    output.seek(0)

    while pattern == output.read() or not (len(result) > 0 and result[0] in ['⬜', '🟨', '🟩']):
        output.seek(0)
        result = output.read()
        output = open('output.txt', 'r+', encoding='utf-8')
    
    output.close()

def writeBestWord():
    output = open('output.txt', 'w', encoding='utf-8')
    output.write(best_word)

#findBestWord()
#print(best_word)
#The best word is TAREI, with an entropy of 6.41

def solve():
    global best_word, max_entropy, result
    waitResult()
    removeWord()
    findBestWord()
    writeBestWord()

best_word = "TAREI"

def write_tarei():
    f = open('output.txt', 'w', encoding='utf-8')
    f.write("TAREI")

def auto():
    write_tarei()
    while not result == '🟩🟩🟩🟩🟩':
        solve()

import sys
from random import *

def unigramAnalysis(filename, freq):
    with open(filename, 'r') as f:
        text = f.read()
        wordlist = text.split()
        for word in wordlist:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1
    return freq


def bigramAnalysis(filename, freq):
    with open(filename, 'r') as f:
        text = f.read()
        wordlist = text.split()
        for word1, word2 in zip(wordlist[:-1], wordlist[1:]):
            pair = word1 + " " + word2
            if pair not in freq:
                freq[pair] = [1, word1, word2]
            else:
                freq[pair][0] += 1
    return freq

def trigramAnalysis(filename, freq):
    with open(filename, 'r') as f:
        text = f.read()
        wordlist = text.split()
        for word1, word2, word3 in zip(wordlist[:-2], wordlist[1:-1], wordlist[2:]):
            pair = word1 + " " + word2 + " " + word3
            if pair not in freq:
                freq[pair] = [1, word1, word2, word3]
            else:
                freq[pair][0] += 1
    return freq
def generateUnigramText(frequency, amount):
    generatedtext = str()

    for _ in range(amount):
        total = 0
        for entry in frequency:
            total += frequency[entry]
        num = randint(1, total) # Generate a number between 1 and the total amount of words.
        current = 0
        for word in frequency:
            current += frequency[word]
            if current >= num:
                generatedtext += word + " "
                break

    print(generatedtext)

def generateNgramText(frequency, amount):
    generatedtext = str()

    total = 0
    for entry in frequency:
        total += frequency[entry][0]
    num = randint(1, total) # Generate a number between 1 and the total amount of words.
    current = 0
    for entry in frequency:
        current += frequency[entry][0]
        if current >= num:
            generatedtext += entry + " "
            lastword = frequency[entry][len(frequency[entry])-1]
            break

    for _ in range(amount - 1):
        validlist = dict()
        total = 0
        for entry in frequency:
            if frequency[entry][1] == lastword:
                total += frequency[entry][0]
                validlist[entry] = frequency[entry]

        num = randint(1, total) # Generate a number between 1 and the total amount of words.
        current = 0
        for entry in validlist:
            current += validlist[entry][0]
            if current >= num:
                for word in validlist[entry][2:]:
                    generatedtext += word + " "
                lastword = validlist[entry][len(validlist[entry])-1]
                break

    print(generatedtext)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        unigram_freq = dict()
        bigram_freq = dict()
        trigram_freq = dict()
        for filename in sys.argv[1:]:
            unigram_freq = unigramAnalysis(filename, unigram_freq)
            bigram_freq = bigramAnalysis(filename, bigram_freq)
            trigram_freq = trigramAnalysis(filename, trigram_freq)

        print("\nUnigram Generated:")
        generateUnigramText(unigram_freq, 100)
        print("\nBigram Generated:")
        generateNgramText(bigram_freq, 99)
        print("\nTrigram Generated:")
        generateNgramText(trigram_freq, 50)



    else:
        print("No filenames given in arguments given.")

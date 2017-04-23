import sys
from random import *

# n-gram.py
# Run by passing the names of *.txt files as arguments. These text files will be analyzed
# and be used to generate new text based off of the frequencies.

# Analysis:
# Frequency is the number times the n-gram appears in the text.
# a unigram is a single word, bigram is each word pair that appears next to each other,
# and a trigram is like a bigram but with 3 words.

# Generation:
# For a unigram each word is simply generated randomly.
# For a bigram and trigram, each new n-gram's first word must match the last word of the last n-gram.


# Takes a filename and analyzes the frequency of the unigrams and adding them to the dictionary freq.
def unigramAnalysis(filename, freq):
    with open(filename, 'r') as f:
        text = f.read()
        wordlist = text.split()
        for word in wordlist:
            if word not in freq:
                freq[word] = 1 # frequency is the number of times the word shows up.
            else:
                freq[word] += 1
    return freq

# Takes a filename and analyzes the frequency of the bigrams (each pair of words) and adding them to the dictionary freq.
def bigramAnalysis(filename, freq):
    with open(filename, 'r') as f:
        text = f.read()
        wordlist = text.split()
        for word1, word2 in zip(wordlist[:-1], wordlist[1:]): # for each word pair.
            pair = word1 + " " + word2 # key is the two words seperated by a space.
            if pair not in freq:
                freq[pair] = [1, word1, word2] # each key stores a list with the frequency (number of times it shows up) and the two words.
            else:
                freq[pair][0] += 1
    return freq

# Takes a filename and analyzes the frequency of the trigrams (each group of 3 words) and adding them to the dictionary freq.
def trigramAnalysis(filename, freq):
    with open(filename, 'r') as f:
        text = f.read()
        wordlist = text.split()
        for word1, word2, word3 in zip(wordlist[:-2], wordlist[1:-1], wordlist[2:]): # for each group of 3 words next to each other.
            pair = word1 + " " + word2 + " " + word3 # key is the three words seperated by a space.
            if pair not in freq:
                freq[pair] = [1, word1, word2, word3] # each key stores a list with the frequency (number of times it shows up) and the three words.
            else:
                freq[pair][0] += 1
    return freq

# Generates the based off of the given frequencies of the amount given.
# Gets total amount of words and generates a number between 1 and that.
# Loops through each frequency adding its number and generates the word if current number >= random number
def generateUnigramText(frequency, amount):
    generatedtext = str()

    for _ in range(amount): # Loops the number of times in amount.
        total = 0
        for entry in frequency: # Gets the total number of words.
            total += frequency[entry]
        num = randint(1, total) # Generate a number between 1 and the total amount of words.
        current = 0
        for word in frequency:
            current += frequency[word] # For each word add the frequency to the current amount.
            if current >= num: # If current amount is >= random number then add word to generated text.
                generatedtext += word + " "
                break

    print(generatedtext)

# Generates text based off of bigram or trigram frequency.
# Each bigram or trigram's first word must match the last word.
# amount determines number of loops.
# Each bigram generates 1 word besides the first which generates 2 words.
# Each trigram generates 2 words besides the first which generates 3 words.
def generateNgramText(frequency, amount):
    generatedtext = str()

    # Initialization generates the first words and gets a last word used for further generation.
    total = 0
    for entry in frequency:
        total += frequency[entry][0]
    num = randint(1, total) # Generate a number between 1 and the total amount of words.
    current = 0
    for entry in frequency:
        current += frequency[entry][0]
        if current >= num:
            generatedtext += entry + " "
            lastword = frequency[entry][len(frequency[entry])-1] # Last word for this freqency is at the end of the list.
            break

    # Main loop.
    for _ in range(amount - 1):
        validlist = dict()
        total = 0
        for entry in frequency: # Generate a valid list of words (where the first word matches the last word of the last generation)
            if frequency[entry][1] == lastword:
                total += frequency[entry][0]
                validlist[entry] = frequency[entry]

        num = randint(1, total) # Generate a number between 1 and the total amount valid of words.
        current = 0
        for entry in validlist: #
            current += validlist[entry][0] # For each entry add the frequency to the current amount.
            if current >= num: # If current amount is >= random number
                for word in validlist[entry][2:]: # For each word besides the first (which matches the last word) add the words.
                    generatedtext += word + " "
                lastword = validlist[entry][len(validlist[entry])-1] # Update last word.
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

        print("\nDistinct Words: {}".format(len(unigram_freq)))
        print("\nBigrams: {}".format(len(bigram_freq)))
        print("\nTrigrams: {}".format(len(trigram_freq)))

        print("\nUnigram Generated:")
        generateUnigramText(unigram_freq, 100)
        print("\nBigram Generated:")
        generateNgramText(bigram_freq, 99)
        print("\nTrigram Generated:")
        generateNgramText(trigram_freq, 50)



    else:
        print("No filenames given in arguments given.")

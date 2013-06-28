#!/usr/bin/env python

import sys
from random import randint, choice 
import re

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains = {}
    corpus = corpus.split()
    
    for i in range(0, len(corpus) - 2):
        word_pair = (corpus[i], corpus[i + 1])
        chains[word_pair] = chains.get(word_pair, [])
        chains[word_pair].append(corpus[i + 2])
    return chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    random_pair = choice(chains.keys())
    while random_pair[0][0].isupper() == False:
        random_pair = choice(chains.keys())         # Choose random key from dictionary

    random_text = [random_pair[0], random_pair[1]]

    while random_text[-1][-1] != ".":   # Keep the chain going till there's a period.
        # Randomly select next word from the dictionary of key/value pairs
        # Where value = list of all possible next words
        new_word_index = randint(0, len(chains[random_pair]) - 1)
        # Get the value (the actual word) given the randomly selected index position
        new_word = chains[random_pair][new_word_index]
        # Append the new word to the string random_text
        random_text.append(new_word)
        # Assign the last two words in random_text to be the new tuple/key          
        random_pair = (random_text[-2], random_text[-1])

    return random_text
 
def main():
    args = sys.argv
    script, filename = args
    corpus = open(filename).read()

    chain_dict = make_chains(corpus)
    random_text = make_text(chain_dict)
    print " ".join(random_text)     # So that the text prints out nicely.

if __name__ == "__main__":
    main()
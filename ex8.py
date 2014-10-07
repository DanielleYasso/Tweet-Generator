#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    d = {}
    words = corpus.split()
    # using range and length of words list
    # for index in range(len(words)-2):
    #     try:
    #         first, second, third = words[index], words[index+1], words[index+2]
    # or, using enumerate:
    for i, word in enumerate(words):
        try:
            first, second, third = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = (first, second)
        d.setdefault(key, []).append(third)

    # empty_list = filter(lambda x: "" in x[0], d.keys())
    # print empty_list

    return d

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    # Filter keys for those that contain starts of sentences
    # sentence_start_list = [key for key in chains.keys() if key[0][0].isupper()]
    sentence_start_list = filter(lambda x: x[0][0].isupper(), chains.keys())
    key = random.choice(sentence_start_list)

    new_text = []
    # unpack key into first and second words and add to print list
    first, second = key
    new_text.extend([first, second])

    # define end of sentence for when to stop while loop below
    e_o_s = ['.', '!', '?']

    while True:
        try:
            # get third word from list of words for key
            third = random.choice(chains[key])
        except KeyError:
            break

        # add words to text to be printed
        new_text.append(third)

        # if third was end of sentence, break
        if third[-1] in e_o_s:
            break
            
        # update key for next loop
        key = (second, third)
        # update second variable for use in next key update
        second = key[1]

    return " ".join(new_text)

def main():
    args = sys.argv
    filename = args[1] 

    # Change this to read input_text from a file
    f = open(filename)
    input_text = f.read()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
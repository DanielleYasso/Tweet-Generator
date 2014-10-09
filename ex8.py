#!/usr/bin/env python

import sys
import random

def make_chains(corpus, num_gram):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    
    d = {}
    words = corpus.split()

    # using enumerate:
    # for i, word in enumerate(words):
    for i in range(len(words)-num_gram):
        word_list = []
        for index in range(num_gram + 1):
            word_list.append(words[i + index])
        key = tuple(word_list[:-1])
        d.setdefault(key, []).append(word_list[-1])
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
    word_list_for_key = list(key)

    new_text.extend(list(key))

    # define end of sentence for when to stop while loop below
    e_o_s = ['.', '!', '?']


    while True:

        # get a word from list of words for key
        last = random.choice(chains.get(key, "...um..."))
        character_count_check = new_text + [last]
        character_count = " ".join(character_count_check)
        characters = len(character_count)

        # add words to text to be printed
        if characters > 140:
            return " ".join(new_text)

        new_text.append(last)
        # character_count = len(" ".join(new_text))

        # # if last was end of sentence, break
        # if character_count >= 140:
        #     break
        if last[-1] in e_o_s:
            break
            
        # update word_list_for_key and key for next loop
        word_list_for_key.append(last)
        word_list_for_key = word_list_for_key[1:]
        key = tuple(word_list_for_key)

    return " ".join(new_text)
    # return "hi"

def main(args):
    # args = sys.argv

    input_text = ""

    for filename in args[1:]:
        f = open(filename)
        input_text += f.read()

    num_gram = int(raw_input("how many words per key would you like? "))

    chain_dict = make_chains(input_text, num_gram)
    random_text = make_text(chain_dict)
    return random_text

if __name__ == "__main__":
    args = sys.argv
    main(args)





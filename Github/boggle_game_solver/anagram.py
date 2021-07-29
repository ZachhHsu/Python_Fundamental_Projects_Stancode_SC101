"""
File: anagram.py
Name: Zach Hsu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                                             # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'                                 # This is the filename of an English dictionary
EXIT = '-1'                                             # Controls when to stop the loop

# Global Variable
anagram_lst = []                                        # Contains all anagrams


def main():
    """
    This program allows users to input a vocabulary, and displays all related anagrams.
    """
    start = time.time()

    print('Welcome to stanCode "Anagram Generator"(or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        read_dictionary(word)
        ans_lst = find_anagrams(word)
        print(len(ans_lst), 'anagrams:', ans_lst)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    """
    This function reads the file and add all vocabularies to a list.
    """
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == len(s):
                if line[0] and line[1] and line[-1] in s:
                    anagram_lst.append(line)


def find_anagrams(s):
    """
    :param s: str, word to be processed
    :return: list, all possible anagrams
    """
    print('Searching...')
    return find_anagrams_helper(s, '', '', [])


def find_anagrams_helper(s, index, current_word, ans_lst):
    if has_prefix(current_word):
        # Base Case
        if len(index) == len(s):
            if current_word not in ans_lst:                 # make sure each anagram is not repeated
                if current_word in anagram_lst:             # make sure current word is an anagram
                    print('Found:', current_word)
                    print('Searching...')
                    ans_lst.append(current_word)

        # Recursive
        else:
            for i in range(len(s)):
                if str(i) not in index:                     # make sure each character of the input word is included
                    # Choose
                    current_word += s[i]

                    # Explore
                    find_anagrams_helper(s, index+str(i), current_word, ans_lst)

                    # Un-choose
                    current_word = current_word[:len(current_word)-1]
    return ans_lst


def has_prefix(sub_s):
    """
    :param sub_s: str, prefix to be checked
    :return: bool, True if start with the prefix; otherwise, false.
    """
    for words in anagram_lst:
        if words.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

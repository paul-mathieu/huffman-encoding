# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:03:48 2020

@author: paul-mathieu
"""

import os

from functools import reduce

#import time

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART I : Algorithm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def path_to_string(path):
    '''
    Converts a text file to a string
    
    
    Input
    ----------
    path : str
        path of the file
        
        
    Output
    ----------
    '' : str
        string of the text
        
    '''

    with open (path, "r") as myfile:
        #reduce to convert a list of string into a single string
        return reduce(lambda x, y : x + y, myfile.readlines())


# =============================================================================
# Alphabet creation
# =============================================================================

def frequency_alphabet(string_txt):
    '''
    Create a frequency alphabet
    
    Input
    ----------
    text : str
        string
    
    
    Output
    ----------
    list_alphabet : list
        list of tuple which contains sorted tuple
        tuple => letter, frequency
        each letter is sorted by frequency and then by ascii

    '''
    
#    t = time.time()
#    list_alphabet = Counter(string_txt).most_common()
    list_alphabet = dict()
    for letter in string_txt:
        if letter in list_alphabet.keys():
            list_alphabet[letter] += 1
        else:
            list_alphabet[letter] = 1
    list_alphabet = list(zip(list_alphabet.keys(),list_alphabet.values()))
    
#    print(list_alphabet)
    
    list_frequency_values = sorted(list(set([value[1] for value in list_alphabet])), reverse = True)
    print(list_frequency_values)
    
    list_alphabet_temp = []
    list_alphabet_final = []
    
    #for each frequency
    for value_frequency in list_frequency_values:
        #letter sorted
        list_alphabet_temp = sorted([element[0] for element in list_alphabet if element[1] == value_frequency], key = ord)
        #tuple sorted
        list_alphabet_temp = [(element, value_frequency) for element in list_alphabet_temp]
        #append
        list_alphabet_final.append(list_alphabet_temp[0])
#        print(list_alphabet_final)
#    print(time.time() - t)
    
    return list_alphabet_final

# =============================================================================
# Création de l'arbre
# =============================================================================

class Tree:
    
    def __init__(self, letter, value = None, left_child = None, right_child = None):
        '''
        Initialisation of the object
        
        Input
        ----------
        letter : str
            letter of the leaf
        value : int
        left_child : Tree
        right_child : Tree
        '''
        
        self.letter = letter
        
        self.left_child = left_child
        self.right_child = right_child
        
        if not value is None:
            #value of the node (if leaf)
            self.value = value
        else:
            #value of the node (if not leaf)
            left_child_value = self.left_child.value if not self.left_child.value is None else 0
            right_child_value = self.right_child.value if not self.right_child.value is None else 0
            #sum of value at the right and at the left
            self.value = left_child_value + right_child_value
    
    def alphabet_to_dag(self, alphabet):
        '''                                                                                                                                                                                                                                                                                                  

path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/') + '/data'
file = '/alice.txt'

#print('path : ' + path)
#print('file : ' + file)

string_txt = path_to_string(path + file)

#print('string : ' + string_txt)

# =============================================================================
# Alphabet
# =============================================================================

frequency_a = frequency_alphabet(string_txt)
#print(len(frequency_a))
print(frequency_a)





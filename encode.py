# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:03:48 2020

@author: paul-mathieu
"""

import os

from functools import reduce
from collections import Counter


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

def frequency_alphabet(text):
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
    list_alphabet = Counter(string_txt).most_common()
#    print(list_alphabet)
    
    list_frequency_values = sorted(list(set([value[1] for value in list_alphabet])))
#    print(list_frequency_values)
    
    #for each frequency
    for value_frequency in list_frequency_values:
        
        
        for 
            if machin < value_frequency:
                break
    
    return list_alphabet

def sort_alphabet(alphabet):
    '''
    Sort an alphabet
    
    Input
    ----------
    dict_alphabet : dict
    
    
    Output
    ----------
    list_alphabet : list
        list of tuple which contains sorted tuple
        tuple => letter, frequency
        each letter is sorted by frequency and then by ascii
    '''
#    sorted_list_alphabet = Counter(dict_alphabet).most_common()
##    sorted(liste, key = ord)
#    for key, value in dict_alphabet.items():
#        pass
#    
#    return sorted_list_alphabet
    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PART II : Application
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# =============================================================================
# Transformation of the text file into string
# =============================================================================

path = os.path.dirname(os.path.abspath(__file__)).replace('\\','/') + '/data'
file = '/textesimple.txt'

print('path : ' + path)
print('file : ' + file)

string_txt = path_to_string(path + file)

print('string : ' + string_txt)

# =============================================================================
# Alphabet
# =============================================================================

frequency_a = frequency_alphabet(string_txt)
print(frequency_a)





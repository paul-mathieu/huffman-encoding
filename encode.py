# -*- coding: utf-8 -*-
"""
@author: paul-mathieu
"""

import os
import time
from functools import reduce


class HuffmanCoding:
    """
    Huffman encoding allows you to compress a text file.
    This class returns a file encoded in .bin format.

    functions
    ----------
    __init__(self, path, file, export_file=None)
        file initialization
    set_dictionary(self)
        creates a class attribute containing the frequency dictionary
    set_text(self)
        creates a class attribute containing the original text (in ascii)
    path_to_string(self)
        uses a local file and returns a character string corresponding to the content
    frequency_alphabet(self)

    sorted_alphabet(self, list_alphabet=None)

    binary_list(self)

    binary_alphabet(self, binary_list=None, binary_dict=None, binary_code='')

    encode_file_txt(self, destination=None)

    encode_file_bin(self, destination=None)

    export_binary_alphabet(self)

    export_freq_alphabet(self)

    compression_ratio(self, original_file=None, encoded_file=None)

    average_character_size(self)

    decode(self, encoded_file=None, destination=None)

    """

    def __init__(self, path, file, export_file=None):
        """
        file initialization
        """
        self.export_file = export_file
        self.path = path + file
        self.dictionary = None
        self.text = None
        self.current_directory = path

        self.file_name = file[len(file) - file[::-1].index('/'):len(file) - file[::-1].index('.') - 1]

        if self.export_file is None:
            self.export_file = '/encoded/' + \
                               self.file_name + \
                               '_comp.bin'

    def set_dictionary(self):
        """
        creates a class attribute containing the frequency dictionary
        """
        self.dictionary = self.frequency_alphabet_init()

    def set_text(self):
        """
        creates a class attribute containing the original text (in ascii)
        """
        self.text = self.path_to_string()

    def path_to_string(self):
        """
        Converts a text file to a string

        Input
        ----------
        path : str
            path of the file

        Output
        ----------
        '' : str
            string of the text
        """
        with open(self.path, "r") as file:
            # reduce to convert a list of string into a single string
            return reduce(lambda x, y: x + y, file.readlines())

    # =============================================================================
    # Alphabet creation
    # =============================================================================

    def frequency_alphabet(self):
        """
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
        """

        self.set_text()
        list_alphabet = dict()
        for letter in self.text:
            if letter in list_alphabet.keys():
                list_alphabet[letter] += 1
            else:
                list_alphabet[letter] = 1
        # transformation of dict to liste
        list_alphabet = list(zip(list_alphabet.keys(), list_alphabet.values()))

        return list_alphabet

    def sorted_alphabet(self, list_alphabet=None):
        """
        Sort an alphabet

        Input
        ----------
        list_alphabet: list
            list of tuple, the first element is a string or a tuple and the second element is a value

        Output
        ----------
        list_alphabet_final: list
            list of tuple, the first element is a string or a tuple and the second element is a value
        """

        if list_alphabet is None:
            list_alphabet = self.frequency_alphabet()
        # remove doublons and sort in reverse
        list_frequency_values = sorted(list(set([value[1] for value in list_alphabet])), reverse=True)

        list_alphabet_temp_ascii = []
        list_alphabet_temp_other = []
        list_alphabet_final = []

        # for each frequency
        for value_frequency in list_frequency_values:
            # letter sorted
            list_alphabet_temp_ascii = sorted(
                [element[0] for element in list_alphabet if element[1] == value_frequency and type(element[0]) == str],
                key=ord, reverse=True)
            # tuple sorted
            list_alphabet_temp_other = [element[0] for element in list_alphabet if
                                        element[1] == value_frequency and not type(element[0]) == str]
            # letters in tuple
            list_alphabet_temp_ascii = [(element, value_frequency) for element in list_alphabet_temp_ascii]
            # tuples in tuples
            list_alphabet_temp_other = [(element, value_frequency) for element in list_alphabet_temp_other]
            #            print('list_alphabet_temp_ascii')
            #            print(list_alphabet_temp_ascii)
            # append
            list_alphabet_final += list_alphabet_temp_ascii
            list_alphabet_final += list_alphabet_temp_other
        #        print(list_alphabet_final)

        return list_alphabet_final

    def binary_list(self):
        """
        A binary list is a dag compsed with tuple in list with tuple.
        A dag is a tree.
        It permits deduce the binary alphabet

        Input
        ----------
        self

        Output
        ----------
        alphabet : list of tuple
        """
        alphabet = self.sorted_alphabet()
        while len(alphabet) > 2:
            # take the two smaller ones (divide the alphabet in half)
            first_part, second_part = alphabet[:-2], alphabet[-2:]
            # create new node
            if len(alphabet) == 2:
                new_node = (second_part, 0)
            else:
                new_node = (second_part, second_part[0][1] + second_part[1][1])
            # add it to the alphabet
            first_part.append(new_node)
            # sort the alphabet
            alphabet = self.sorted_alphabet(first_part)

        # return the dag
        return alphabet

    def binary_alphabet(self, binary_list=None, binary_dict=None, binary_code=''):
        """
        Using recursivity

        Input
        ----------
        binary_list: list of tuple
            cf. function, used to browse the tree

        binary_dict: list of tuple
            dictionary with binary values, used for in recursion then is returned

        Output
        ----------
        binary_dict: list of tuple
            dictionary with binary values, used for in recursion then is returned
        """
        if binary_list is None:
            binary_list = self.binary_list()
        if binary_dict is None:
            binary_dict = dict()

        for element in binary_list:
            binary_code_init = binary_code
            # if it's str
            if not type(element) == int:
                # if it's not a leaf
                if type(element[1]) == int:
                    binary_value_to_add = str(binary_list.index(element))
                    binary_value_to_add = '1' if binary_value_to_add == '0' else '0'
                else:
                    binary_value_to_add = ''
                # if it's a leaf
                if type(element[0]) == str:
                    # add value to the dict
                    binary_dict[element[0]] = (binary_code_init + binary_value_to_add)  # [::-1]
                # if it's not a leaf
                else:
                    self.binary_alphabet(element, binary_dict, binary_code_init + binary_value_to_add)

        return binary_dict

    # =============================================================================
    # Encoding
    # =============================================================================

    def encode_file_txt(self, destination=None):
        """
        Export the encoded file in false binary format (txt)

        Input
        ----------
        destination: string
            path for the encode file
        """
        if destination is None:
            destination = self.current_directory + '/encoded/encode.txt'

        binary_alphabet = self.binary_alphabet()

        file = open(destination, "w")
        for letter in self.text:
            file.write(binary_alphabet[letter])
        file.close()

    def encode_file_bin(self, destination=None):
        """
        Export the encoded file in binary format

        Input
        ----------
        destination: string
            path for the encode file

        """
        if destination is None:
            destination = self.current_directory + self.export_file

        binary_alphabet = self.binary_alphabet()
        binary_text = ''

        for letter in self.text:
            binary_text += binary_alphabet[letter]
        length_binary_text = len(binary_text)

        file = open(destination, "wb")

        index_begin = 0
        while index_begin + 9 <= length_binary_text:
            octet = binary_text[index_begin:index_begin + 8]
            index_begin += 8
            #            print(octet)
            file.write(int(octet, 2).to_bytes(len(octet) // 8, byteorder='big'))
        # management of the last character whose size is not necessarily equal to 8
        # '0' * 0 if it's the last octet
        octet = binary_text[index_begin:] + '0' * (8 - len(binary_text[index_begin:]))
        file.write(int(octet, 2).to_bytes(-(-len(octet) // 8), byteorder='big'))

        file.close()

    # =============================================================================
    # Other exports
    # =============================================================================

    def export_binary_alphabet(self):
        """
        Export the binary alphabet as a text file.
        The values​are the character and their binary code.
        They are separated by tabs and by newlines.

        Input
        ----------
            self
        """
        dict_values = self.binary_alphabet()
        dict_to_list = list(zip(dict_values.keys(), dict_values.values()))
        destination = self.current_directory + '/encoded/' + self.file_name + '_bin.txt'

        file = open(destination, "w")

        # special characters are replaced
        for couple_dict in dict_to_list:
            if couple_dict[1] == '\n':
                couple_dict[1] = '[enter]'
            elif couple_dict[1] == '\t':
                couple_dict[1] = '[tab]'
            elif couple_dict[1] == ' ':
                couple_dict[1] = '[space]'

            file.write(couple_dict[0] + '\t' + couple_dict[1] + '\n')

        file.close()

    def export_freq_alphabet(self):
        """
        Export the frequency alphabet as a text file.
        The values​are the character and their frequency of appearance.
        They are separated by tabs and by newlines.
        The first line is the number of characters

        Input
        ----------
            self
        """
        list_values = self.sorted_alphabet()[::-1]
        destination = self.current_directory + '/encoded/' + self.file_name + '_freq.txt'

        file = open(destination, "w")

        file.write(str(len(list_values)) + '\n')
        for character, value in list_values:
            if character == '\n':
                character = '[enter]'
            elif character == '\t':
                character = '[tab]'
            elif character == ' ':
                character = '[space]'

            file.write(character + '\t' + str(value) + '\n')

        file.close()

    # =============================================================================
    # Statistics
    # =============================================================================

    def compression_ratio(self, original_file=None, encoded_file=None):
        """
        The compression ratio is the file size gained compared to the original file.

        Input
        ----------
        original_file: string
            path of the original file

        encoded_file: string
            path of the encoded file

        Output
        ----------
        : float
            Decimal value of the ratio.
        """
        if original_file is None:
            original_file = self.path
        if encoded_file is None:
            encoded_file = self.current_directory + self.export_file

        original_file_exist = os.path.isfile(original_file)
        encoded_file_exist = os.path.isfile(encoded_file)
        if original_file_exist:
            length_original_file = os.path.getsize(original_file)
        else:
            print("The path of the original file is incorrect.")

        if encoded_file_exist:
            length_encoded_file = os.path.getsize(encoded_file)
        else:
            print("The path of the encoded file is incorrect or may not exist.")

        if original_file_exist and encoded_file_exist:
            return round(1 - length_encoded_file / length_original_file, 6)
        else:
            return None

    def average_character_size(self):
        """
        Average size of characters once encoded.

        Input
        ----------
        self

        Output
        ----------
        average size in bits/chr
        """
        # utilisation de freq alphabet et de binary alphabet
        binary_alphabet = encoding.binary_alphabet()
        frequency_alphabet = dict(encoding.frequency_alphabet())

        len_mean = sum([len(binary_alphabet[key]) * frequency_alphabet[key] for key in binary_alphabet.keys()]) / sum(
            list(frequency_alphabet.values()))

        return len_mean

    # =============================================================================
    # Decoding
    # =============================================================================

    def decode(self, encoded_file=None, destination=None):
        """
        Decode the binary file using the binary alphabet

        Input
        ----------
        encoded_file: string
            path of the binary file

        destination: string
            path for the decoded file
        """

        if destination is None:
            destination = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/encoded/decode.txt'

        if encoded_file is None:
            encoded_file = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + self.export_file

        with open(encoded_file, "rb") as file:
            # reduce to convert a list of string into a single string
            encoded_text = reduce(lambda x, y: x + y, file.readlines())
            file.close()

        # print(encoded_text[:8])
        # for element in encoded_text:
        #     print(bin(element))
        # '0' * 0 if it's not the last octet
        encoded_text = ''.join(['0' * (8 - len(bin(element)[2:])) + bin(element)[2:] for element in encoded_text])
        encoded_text, last_octet = encoded_text[:-32], encoded_text[-32:]

        file = open(destination, "w")

        dictionary = self.binary_alphabet()
        dictionary = dict(zip(dictionary.values(), dictionary.keys()))

        # print(list(dictionary.values()))
        octet_found = False
        while not octet_found:
            value = last_octet
            while not value == "":
                if value in dictionary.keys():
                    octet_found = True
                    break
                value = value[1:]
                # print(value)
            # if last octet not found
            # (never append but it's better)
            if last_octet == '' or octet_found:
                break
            last_octet = last_octet[:-1]
        encoded_text += last_octet

        while encoded_text:
            # print(dictionary.keys())
            if len(encoded_text) < 8:
                break
            for key in list(dictionary.keys()):
                # print(encoded_text[:len(key)])
                # print(key)
                if encoded_text[:len(key)] == key:
                    # print(key)
                    # print(dictionary[key], end = '')
                    file.write(dictionary[key])
                    encoded_text = encoded_text[len(key):]
                    break

        # print(encoded_text)
        # file.write(encoded_text)
        file.close()


# =============================================================================
# Utilisation
# =============================================================================

# time
t = time.time()
print('Initialisation...')

# ~~~~ file name ~~~~ #

path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
# file = '/data/alice.txt'
file = '/data/textesimple.txt'
# file = '/data/textesimple_sans_espaces.txt'

# print('path : ' + path)
# print('file : ' + file)


# ~~~~ initialisation ~~~~ #

encoding = HuffmanCoding(path, file)

# print(encoding.sorted_alphabet())

# print (encoding.text)

# print(encoding.binary_list())
print(encoding.binary_alphabet())
# print(encoding.frequency_alphabet())


# ~~~~ export ~~~~ #

print('Exporting...')

encoding.encode_file_bin()
# encoding.encode_file_txt()
encoding.export_freq_alphabet()
# encoding.export_binary_alphabet()

print('Compression Ratio: ', end='')
print(encoding.compression_ratio())

print('Average Size: ', end='')
print(round(encoding.average_character_size(), 5), end=' ')
print('bits/chr')

# ~~~~ decoding ~~~~ #
print('Exit...')

# encoding.decode()


t = time.time() - t
print('Processing Time: ', end='')
print(str(round(t * 1000, 3)) + 'ms')

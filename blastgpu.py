import numpy
import time
import math
import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
from blastFunc import *


def get_index_table(query_sequence, length):
    dictionary = k_letter_words(query_sequence, length)
    list_lesser3 = []
    list_more3 = []
    for seq in dictionary:
        if len(dictionary[seq]) >= 3:
            list_more3.append([seq, dictionary[seq]])
        else:
            list_lesser3.append([seq, dictionary[seq]])
    return [list_lesser3, list_more3]


def get_presence_vector(query):
    presence = "0" * (22 ** 3)
    subs_mat = BLOOSUM62()
    words_positions = {}
    counter = 0
    for amino_x in subs_mat.dictionary:
        for amino_y in subs_mat.dictionary:
            for amino_z in subs_mat.dictionary:
                word = amino_x + amino_y + amino_z
                words_positions[counter] = word
                counter += 1

    for index in range(len(presence)):
        if words_positions[index] in query:
            presence[index] = "1"

    return presence





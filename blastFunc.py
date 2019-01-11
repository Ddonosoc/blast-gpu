from BLOOSUM62 import *
import re
import math

T = 19
X = 3
L = 0.318
K = 0.13
Length = 2000000


def k_letter_words(sequence, length):
    words = []
    dict = {}
    for i in range(len(sequence) - length + 1):
        word = sequence[i: i + length]
        if '#' in word:
            continue
        words.append(word)
        if word in dict:
            dict[word].append(i)
        else:
            dict[word] = [i]
    return dict


# Return a dictionary of possibles words with score at least T
def get_HSW(word, T):
    dict = {}
    data = BLOOSUM62()
    for i in data.dictionary:
        for j in data.dictionary:
            for k in data.dictionary:
                searching = i + j + k
                scoring = data.score(word, searching)
                if scoring >= T:
                    dict[i + j + k] = scoring

    return dict


# Return indices of the word in the sequence
def get_hits(word, sequence):
    hits = [m.start() for m in re.finditer(word, sequence)]
    return hits


def get_lesser(indices_list, index):
    for i in range(len(indices_list)):
        if indices_list[i] > index:
            return i - 1
        elif indices_list == index:
            return i


# Extends a word in a sequence until it decreases
def extend_hit(sequence, query_sequence, index_word, index_hit, score, length, X):
    data = BLOOSUM62()
    counter = 1
    extension = ''
    repeat = True
    while repeat:
        can = (index_word - counter >= 0) and (index_word + length + counter <= len(query_sequence)) and\
              (index_hit - counter >= 0) and (index_hit + length + counter <= len(sequence))
        if not can:
            break
        new_word = query_sequence[index_word - counter: index_word + length + counter]
        new_seq = sequence[index_hit - counter: index_hit + length + counter]
        if '#' in new_word or '#' in new_seq:
            break
        new_score = data.score(new_word, new_seq)
        repeat = (new_score >= score - X)
        score = new_score if repeat else score
        extension = new_seq if repeat else extension
        counter = counter + 1 if repeat else counter
    if len(extension) > 0:
        return [extension, score, counter]
    else:
        return None


def get_bit_score(score):
    global L, K
    return (L * score - math.log(K)) / math.log(2)


def e_value(bit_score, query_length):
    global Length
    return Length * query_length / (2 ** bit_score)


def search_s(sequence):
    database = ''
    with open('./database/database1.txt') as textfile:
        database += textfile.readline()
    positions = get_hits('#', database)
    print(len(database))
    # Hashes tables
    words = k_letter_words(sequence, 3)
    dictionary = {}
    for word in words:
        if word not in dictionary:
            dictionary[word] = get_HSW(word, 17)

    print(dictionary)
    candidates = {}
    viewd = {}

    for word in words:
        for hsw in dictionary[word]:
            matches = get_hits(hsw, database)
            if len(matches) == 0:
                continue
            else:
                for value in matches:
                    if hsw not in viewd:
                        viewd[hsw] = [value]
                    elif value not in viewd[hsw]:
                        viewd[hsw].append(value)
                    else:
                        continue
                    r = get_lesser(positions, value)
                    for pos in words[word]:
                        results = extend_hit(database[positions[r]:positions[r + 1]], sequence, pos, value - positions[r], dictionary[word][hsw], 3, 3)
                        print(results)
                        if word not in candidates:
                            if results is not None:
                                candidates[word] = [results]
                        else:
                            if results not in candidates[word] and results is not None:
                                candidates[word].append(results)

    print(words)
    print(candidates)
    print(len(positions))
    return candidates


# words = k_letter_words('ABCDEFGASJEGUSJLJGIUYNVKNVK', 3)
# print(get_HSW('ABC', 13))
search_s('ABSCEKAA')
print(extend_hit('ACKSDGAGCKAGCAGCA', 'TARNGGAGCTRSNAA', 6, 6, BLOOSUM62().score('AGC', 'AGC'), 3, 3))

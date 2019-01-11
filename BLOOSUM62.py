

class BLOOSUM62:
    Codificacion = "Ala: 0, Arg: 1, Asn: 2, Asp: 3, Cys: 4, Gln: 5, Glu: 6, Gly: 7, His: 8, Ile: 9, Leu: 10, Lys: 11" \
                   "Met: 12, Phe: 13, Pro: 14, Ser: 15, Thr: 16, Trp: 17, Tyr: 18, Val: 19"

    dictionary = {'A': 0, 'R': 1, 'N': 2, 'D': 3, 'C': 4, 'Q': 5, 'E': 6, 'G': 7, 'H': 8, 'I': 9, 'L': 10, 'K': 11,
                  'M': 12, 'F': 13, 'P': 14, 'S': 15, 'T': 16, 'W': 17, 'Y': 18, 'V': 19, 'B': 20, 'Z': 21, 'X': 22}

    def __init__(self):
        self.matrix = [[4],                                                                             # 0
                       [-1, 5],                                                                         # 1
                       [-2, 0, 6],                                                                      # 2
                       [-2, -2, 1, 6],                                                                  # 3
                       [0, -3, -3, -3, 9],                                                              # 4
                       [-1, 1, 0, 0, -3, 5],                                                            # 5
                       [-1, 0, 0, 2, -4, 2, 5],                                                         # 6
                       [0, -2, 0, -1, -3, -2, -2, 6],                                                   # 7
                       [-2, 0, 1, -1, -3, 0, 0, -2, 8],                                                 # 8
                       [-1, -3, -3, -3, -1, -3, -3, -4, -3, 4],                                         # 9
                       [-1, -2, -3, -4, -1, -2, -3, -4, -3, 2, 4],                                      # 10
                       [-1, 2, 0, -1, -3, 1, 1, -2, -1, -3, -2, 5],                                     # 11
                       [-1, -1, -2, -3, -1, 0, -2, -3, -2, 1, 2, -1, 5],                                # 12
                       [-2, -3, -3, -3, -2, -3, -3, -3, -1, 0, 0, -3, 0, 6],                            # 13
                       [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4, 7],                     # 14
                       [1, -1, 1, 0, -1, 0, 0, 0, -1, -2, -2, 0, -1, -2, -1, 4],                        # 15
                       [0, -1, 0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1, 1, 5],                # 16
                       [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1, 1, -4, -3, -2, 11],         # 17
                       [-2, -2, -2, -3, -2, -1, -2, -3, 2, -1, -1, -2, -1, 3, -3, -2, -2, 2, 7],        # 18
                       [0, -3, -3, -3, -1, -2, -2, -3, -3, 3, 1, -2, 1, -1, -2, -2, 0, -3, -1, 4],      # 19
                       [-2, -1, 3, 4, -3, 0, 1, -1, 0, -3, -4, 0, -3, -3, -2, 0, -1, -4, -3, -3, 4],    # 20
                       [-1, 0, 0, 1, -3, 3, 4, -2, 0, -3, -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, 4],  # 21
                       [-1, 0, 0, 1, -3, 3, 4, -2, 0, -3, -3, 1, -1, -3, -1, 0, -1, -3, -2, -2, 1, -1, 2] # 22
                       ]

    """ get the score of two aminoacids using the score matrix"""
    def search(self, i, j):
        if i not in self.dictionary or j not in self.dictionary:
            print("Value not found (one of them): ", i, j)
            exit(-1)
        x = self.dictionary[i]
        y = self.dictionary[j]
        return self.matrix[max(x, y)][min(x, y)]

    """ print the info of the class"""
    def help(self):
        print("CODIFICACION:")
        print(self.Codificacion)
        print("Matriz BLOOSUM 62")
        for elem in self.matrix:
            string = ''
            for value in elem:
                string = string + str(value) + "\t"
            print(string)

    """ get the total score between two sequences"""
    def score(self, query, sequence):
        total = 0
        for i in range(len(query)):
            total += self.search(query[i], sequence[i])
        return total

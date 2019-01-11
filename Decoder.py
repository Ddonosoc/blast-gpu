
class Decoder:
    table = {"GCU": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A', "CGU": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R', "AGA": 'R',
             "AGG": 'R', "AAU": 'N', "AAC": 'N', "GAU": 'D', "GAC": 'D', "UGU": 'C', "UGC": 'C', "CAA": 'Q', "CAG": 'Q',
             "GAA": 'E', "GAG": 'E', "GGU": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G', "CAU": 'H', "CAC": 'H', "AUU": 'I',
             "AUC": 'I', "AUA": 'I', "UUA": 'L', "UUG": 'L', "CUU": 'L', "CUC": 'L', "CUA": 'L', "CUG": 'L', "AAA": 'K',
             "AAG": 'K', "AUG": 'M', "UUU": 'F', "UUC": 'F', "CCU": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P',
             "UCU": 'S', "UCC": 'S', "UCA": 'S', "UCG": 'S', "AGU": 'S', "AGC": 'S', "ACU": 'T', "ACC": 'T', "ACA": 'T',
             "ACG": 'T', "UGG": 'W', "UAU": 'Y', "UAC": 'Y', "GUU": 'V', "GUC": 'V', "GUA": 'V', "GUG": 'V',
             "GCT": 'A', "CGT": 'R', "AAT": 'N', "GAT": 'D', "TGT": 'C', "TGC": 'C', "GGT": 'G', "CAT": 'H', "ATT": 'I',
             "ATC": 'I', "ATA": 'I', "TTA": 'L', "TTG": 'L', "CTT": 'L', "CTC": 'L', "CTA": 'L', "CTG": 'L', "ATG": 'M',
             "TTT": 'F', "TTC": 'F', "CCT": 'P', "TCT": 'S', "TCC": 'S', "TCA": 'S', "TCG": 'S', "AGT": 'S',
             "ACT": 'T', "TGG": 'W', "TAT": 'Y', "TAC": 'Y', "GTT": 'V', "GTC": 'V', "GTA": 'V', "GTG": 'V', "UAG": 'Z',
             "UGA": 'B', "UAA": 'Z', 'TAG': 'Z', 'TGA': 'U', 'TAA': 'Z'}

    def __init__(self):
        self.words = []

    """ Transform a nucleotid sequence to a aminoacid sequence, using stop sequences as Z"""
    def nuc2protein(self, sequence):
        protein = ''
        for i in range(int(len(sequence) / 3)):
            word = sequence[3 * i] + sequence[3 * i + 1] + sequence[3 * i + 2]
            protein += self.table[word]
        return protein

    """ Return a windowed subset of subsequences (with length equal to w) of the given sequence"""
    def seq2words(self, sequence, w):
        words = []
        for i in range(len(sequence) - w + 1):
            words.append(sequence[i] + sequence[i + 1] + sequence[i + 2])
        return words

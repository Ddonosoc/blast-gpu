from Bio import SeqIO

def preprocess():
    for i in range(1, 9):
        string1 = ''
        counter = 0
        print(counter)
        print(i)
        print("GUARDANDO STRING")
        for seq_record in SeqIO.parse("c:/users/diego/desktop/carpetas/u/gpu/proyecto/database/nr", "fasta"):
            if counter <= 250000 * i:
                if not (250000 * (i - 1) <= counter <= 250000 * i):
                    counter += 1
                    continue
                string1 += "#" + str(seq_record.seq)
                counter += 1
                if counter % 10000 == 0:
                    print(counter)
            else:
                break

        print(counter)
        print("GUARDANDO ARCHIVO" + str(i))
        with open("c:/users/diego/desktop/carpetas/u/gpu/proyecto/database/database"+str(i) +".txt", 'w') as file:
            file.write(string1)
        print("ARCHIVO GUARDADO" + str(i))


def orderSequences():
    for i in range(1, 9):
        print("ORDENANDO ARCHIVO", i)
        dictionary = {}
        line = ''
        print("ABRIENDO DATABASE")
        with open("./database/database" + str(i) + ".txt") as readFile:
            line += readFile.readline()

        array = line.split('#')

        for sequence in array:
            n = len(sequence)
            if n not in dictionary:
                dictionary[n] = [sequence]
            else:
                dictionary[n].append(sequence)

        print("OBTENIENDO STRING PARCIALMENTE ORDENADO")
        string = ''
        for value in dictionary:
            if value == 0:
                continue
            for sequence_v in dictionary[value]:
                string += '#' + sequence_v

        print("GUARDANDO STRING")
        with open("./database/database" + str(i) + "_s.txt", 'w') as writeFile:
            writeFile.write(string)


orderSequences()

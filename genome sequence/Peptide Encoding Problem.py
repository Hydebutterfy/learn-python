#Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
# Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
#     Output: All substrings of Text encoding Peptide (if any such substrings exist).
def reverse_string(seq):
    return seq[::-1]

def complement(seq):
#return the complementary sequence string.
    seq=seq.upper()
    basecomplement={"A":"T","C":"G","G":"C","T":"A","N":"N"}
    letters=list(seq)
    letters=[basecomplement[base] for base in letters]
    return ''.join(letters)


def reversecomplement(seq):
    #return the reverse complement of the dna string.
    seq=reverse_string(seq)
    seq=complement(seq)
    return seq

def DNA_To_AA(seq):
    RNA_AA_dict = {'TCC': 'S', 'TAC': 'Y', 'AGT': 'S', 'ACG': 'T', 'TAA': '*', 'TTA': 'L', 'GTC': 'V', 'CAC': 'H',
                   'CGT': 'R', 'CGG': 'R', 'CTC': 'L', 'AGG': 'R', 'ACA': 'T', 'TCA': 'S', 'CCT': 'P', 'CAG': 'Q',
                   'ACC': 'T', 'TTC': 'F', 'ATC': 'I', 'AAT': 'N', 'ATA': 'I', 'CAT': 'H', 'GGC': 'G', 'GGG': 'G',
                   'GCT': 'A', 'GAT': 'D', 'GCA': 'A', 'GCG': 'A', 'GTA': 'V', 'GAC': 'D', 'CTT': 'L', 'CAA': 'Q',
                   'CCG': 'P', 'AAG': 'K', 'GTT': 'V', 'GGT': 'G', 'TAT': 'Y', 'TGG': 'W', 'AGA': 'R', 'TTT': 'F',
                   'TAG': '*', 'TGC': 'C', 'GGA': 'G', 'CCA': 'P', 'GCC': 'A', 'CGA': 'R', 'AAA': 'K', 'GTG': 'V',
                   'CGC': 'R', 'CTG': 'L', 'TCG': 'S', 'TTG': 'L', 'GAA': 'E', 'GAG': 'E', 'TCT': 'S', 'ATT': 'I',
                   'AAC': 'N', 'ACT': 'T', 'TGT': 'C', 'CTA': 'L', 'ATG': 'M', 'CCC': 'P', 'AGC': 'S', 'TGA': '*'}
    F_position = 0
    R_position = 0
    Aa=""
    for i in range(int(len(seq) / 3)):
        F_position = i*3
        R_position = F_position+3
        RNA_one=seq[F_position:R_position]
        #if RNA_one == "TAA" or RNA_one == "TAG" or RNA_one == "TGA":
        #   break
        Aa += RNA_AA_dict[RNA_one]

    return Aa

def Peptide_Encoding(DNA,AA_input):
    AA= DNA_To_AA(DNA)
    #print(AA)
    l=len(AA_input)
    return_DNA=[]
    find_position=0
    #print(DNA,AA,l,return_DNA,find_position)


    while AA_input in AA[find_position:]:
        #print(AA[find_position:])
        AA_position = find_position + AA[find_position:].find(AA_input)
        DNA_position = 3 * AA_position
        #print(AA_position, DNA_position)
        return_DNA.append(DNA[DNA_position:DNA_position + 3 * l])
        find_position = AA_position + 1
        #print(find_position)
    return return_DNA



DNA=input("what is the genome sequence?")
F_position=0
R_position=0

Aa_input=input("what is the aa?")



DNA_F_1=DNA
print1=Peptide_Encoding(DNA_F_1,Aa_input)
if print1!=[]:
    for i in print1:
        print("1",i)


DNA_F_2=DNA[1:]
print2=Peptide_Encoding(DNA_F_2,Aa_input)
if print2!=[]:
    for i in print2:
        print("2",i)

DNA_F_3=DNA[2:]
print3=Peptide_Encoding(DNA_F_3,Aa_input)
if print3!=[]:
    for i in print3:
        print("3",i)

RC_DNA=reversecomplement(DNA)

DNA_R_1=RC_DNA
print4=Peptide_Encoding(DNA_R_1,Aa_input)
if print4!=[]:
    for i in print4:
        print("4",reversecomplement(i))

DNA_R_2=RC_DNA[1:]
print5=Peptide_Encoding(DNA_R_2,Aa_input)
if print5!=[]:
    for i in print5:
        print("5",reversecomplement(i))

DNA_R_3=RC_DNA[2:]
print6=Peptide_Encoding(DNA_R_3,Aa_input)
if print6!=[]:
    for i in print6:
        print("6",reversecomplement(i))

#print(DNA_F_1,DNA_F_2,DNA_F_3,DNA_R_1,DNA_R_2,DNA_R_3)
#print(Aa_F_1,Aa_F_2,Aa_F_3,Aa_R_1,Aa_R_2,Aa_R_3)

#根据AA序列在基因组中寻找相关序列

#RNA_AA_table=[]
#filename = input("Enter file name: ")
#fileread = open(filename, "r")
#for i in fileread:
#    read = i.strip()
#    RNA_AA_table.append(read.upper())
#print(RNA_AA_table)
#RNA_AA_dict={}
#for i in RNA_AA_table:
#    RNA_AA_dict[i[:3]]=i[-1]
#print(RNA_AA_dict)

RNA_AA_dict={'UCC': 'S', 'UAC': 'Y', 'AGU': 'S', 'ACG': 'T', 'UAA': '*', 'UUA': 'L', 'GUC': 'V', 'CAC': 'H',
             'CGU': 'R', 'CGG': 'R', 'CUC': 'L', 'AGG': 'R', 'ACA': 'T', 'UCA': 'S', 'CCU': 'P', 'CAG': 'Q',
             'ACC': 'T', 'UUC': 'F', 'AUC': 'I', 'AAU': 'N', 'AUA': 'I', 'CAU': 'H', 'GGC': 'G', 'GGG': 'G',
             'GCU': 'A', 'GAU': 'D', 'GCA': 'A', 'GCG': 'A', 'GUA': 'V', 'GAC': 'D', 'CUU': 'L', 'CAA': 'Q',
             'CCG': 'P', 'AAG': 'K', 'GUU': 'V', 'GGU': 'G', 'UAU': 'Y', 'UGG': 'W', 'AGA': 'R', 'UUU': 'F',
             'UAG': '*', 'UGC': 'C', 'GGA': 'G', 'CCA': 'P', 'GCC': 'A', 'CGA': 'R', 'AAA': 'K', 'GUG': 'V',
             'CGC': 'R', 'CUG': 'L', 'UCG': 'S', 'UUG': 'L', 'GAA': 'E', 'GAG': 'E', 'UCU': 'S', 'AUU': 'I',
             'AAC': 'N', 'ACU': 'T', 'UGU': 'C', 'CUA': 'L', 'AUG': 'M', 'CCC': 'P', 'AGC': 'S', 'UGA': '*'}

RNA=input("what is the RNA sequence?")
F_position=0
R_position=0
Aa=""
for i in range(int(len(RNA)/3)):
    F_position=i*3
    R_position=F_position+3
    RNA_one=RNA[F_position:R_position]
    if RNA_one=="UAA" or RNA_one=="UAG" or RNA_one=="UGA":
        break
    Aa+=RNA_AA_dict[RNA_one]

print(Aa)




#Protein Translation Problem.txt
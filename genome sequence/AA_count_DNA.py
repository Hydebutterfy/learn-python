RNA_AA_dict={'UCC': 'S', 'UAC': 'Y', 'AGU': 'S', 'ACG': 'T', 'UAA': '*', 'UUA': 'L', 'GUC': 'V', 'CAC': 'H', 'CGU': 'R', 'CGG': 'R', 'CUC': 'L', 'AGG': 'R', 'ACA': 'T', 'UCA': 'S', 'CCU': 'P', 'CAG': 'Q', 'ACC': 'T', 'UUC': 'F', 'AUC': 'I', 'AAU': 'N', 'AUA': 'I', 'CAU': 'H', 'GGC': 'G', 'GGG': 'G', 'GCU': 'A', 'GAU': 'D', 'GCA': 'A', 'GCG': 'A', 'GUA': 'V', 'GAC': 'D', 'CUU': 'L', 'CAA': 'Q', 'CCG': 'P', 'AAG': 'K', 'GUU': 'V', 'GGU': 'G', 'UAU': 'Y', 'UGG': 'W', 'AGA': 'R', 'UUU': 'F', 'UAG': '*', 'UGC': 'C', 'GGA': 'G', 'CCA': 'P', 'GCC': 'A', 'CGA': 'R', 'AAA': 'K', 'GUG': 'V', 'CGC': 'R', 'CUG': 'L', 'UCG': 'S', 'UUG': 'L', 'GAA': 'E', 'GAG': 'E', 'UCU': 'S', 'AUU': 'I', 'AAC': 'N', 'ACU': 'T', 'UGU': 'C', 'CUA': 'L', 'AUG': 'M', 'CCC': 'P', 'AGC': 'S', 'UGA': '*'}
AA_count={}
for value in RNA_AA_dict.values():
    if value not in AA_count.keys():
        AA_count[value]=1
    else:
        AA_count[value]+=1
print(AA_count)

AA_str="VKLFPWFNQY"
total_number=1
for i in AA_str:
    total_number=total_number*AA_count[i]

print(total_number)

#知道氨基酸序列推测有多少种RNA的可能序列
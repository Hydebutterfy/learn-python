#Probabilities={'CCGCGATAATCAGCTTACGC':0.35042556227667176, 'CTTTTGGGATAGAGTGTAAC': 0.33507142169157156, 'ACGAGGTCAGGATAGACCTT': 0.7601613402024883, 'CTGACCTAGATGAACTAGAT': 0.11108805901744734, 'GCACGGACGACCGTTCATGA': 0.18524765369172147, 'GTAGAGCTACGGAAGGCCCA': 0.2011405995567518, 'TTCTCTCTGGACCATCTGCT': 0.2501031420836599, 'ATTACAAGCCCACCCAACGG': 0.919347283940846, 'GAGTGCACTCTTGATGTCTT': 0.075471725559071, 'GGTCGTTTGTATAGTTTCTG': 0.12088135462600524}
Probabilities={"a":0.22,"b":0.54, "c":0.58,"d":0.36,"e":0.3}
def Normalize(Probabilities):
    all_probability=0
    for i in Probabilities.keys():
        #print(i)
        all_probability+=Probabilities[i]
    #print(all_probability)
    for j in Probabilities.keys():
        Probabilities[j]=Probabilities[j]/all_probability


    return Probabilities

print(Normalize(Probabilities))
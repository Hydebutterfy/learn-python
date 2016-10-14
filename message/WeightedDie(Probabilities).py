import random

Probabilities={'CCGCGATAATCAGCTTACGC':0.35042556227667176, 'CTTTTGGGATAGAGTGTAAC': 0.33507142169157156, 'ACGAGGTCAGGATAGACCTT': 0.7601613402024883, 'CTGACCTAGATGAACTAGAT': 0.11108805901744734, 'GCACGGACGACCGTTCATGA': 0.18524765369172147, 'GTAGAGCTACGGAAGGCCCA': 0.2011405995567518, 'TTCTCTCTGGACCATCTGCT': 0.2501031420836599, 'ATTACAAGCCCACCCAACGG': 0.919347283940846, 'GAGTGCACTCTTGATGTCTT': 0.075471725559071, 'GGTCGTTTGTATAGTTTCTG': 0.12088135462600524}

def WeightedDie(Probabilities):
    tem_p=random.uniform(0,1)
    print(tem_p)
    check_p=0
    for i in Probabilities.keys():
        if Probabilities[i]+check_p>=tem_p>=check_p:
            return i
        check_p += Probabilities[i]

print(WeightedDie(Probabilities))




            #There is no restriction on what face you choose depending on the result of sampling from the uniform distribution: that is up to you. The only restriction is that, in your example, your die should output "AA" 20% of the time, "TT" 20% of the time, "CC" 10% of the time, "GG" 10% of the time, and "AT" 40% of the time.
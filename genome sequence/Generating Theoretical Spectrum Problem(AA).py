dict_Cyclospectrum={"G":57,"A":71,"S":87,"P":97,"V":99,"T":101,"C":103,"I":113,"L":113,"N":114,"D":115,"K":128,
                    "Q":128,"E":129,"M":131,"H":137,"F":147,"R":156,"Y":163,"W":186}
#print(dict_Cyclospectrum)

AA=input("what is the AA?")
longer_AA=AA+AA
list_Cyclospectrum=["0"]
for i in range(1,len(AA)):
    #print(i)
    for j in range(len(AA)):
        #print(j)
        temp_aa=longer_AA[j:j+i]
        temp_Cyclospectrum=0
        print(temp_aa)
        for k in temp_aa:
            #print(k)
            temp_Cyclospectrum+=dict_Cyclospectrum[k]
        list_Cyclospectrum.append(str(temp_Cyclospectrum))


temp_Cyclospectrum=0
for i in AA:
    temp_Cyclospectrum+=dict_Cyclospectrum[i]
list_Cyclospectrum.append(str(temp_Cyclospectrum))

#print(list_Cyclospectrum)
print_list=sorted(list_Cyclospectrum)
#print(print_list)

print(' '.join(print_list))

#氨基酸打成片段,算出分子量大小分布,从0-最大。

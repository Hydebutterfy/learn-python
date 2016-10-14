#Counting Peptides with Given Mass Problem: Compute the number of peptides of given mass.
#     Input: An integer m.
#     Output: The number of linear peptides having integer mass m.


mass=int(input("what is the mass?"))
AA_dict_mass={"G":57,"A":71,"S":87,"P":97,"V":99,"T":101,"C":103,"I/L":113,"N":114,"D":115,"K/Q":128,
              "E":129,"M":131,"H":137,"F":147,"R":156,"Y":163,"W":186}

mass_list=sorted(AA_dict_mass.values())

small_number=int(mass/mass_list[-1]+1)
larger_number=int(mass/mass_list[0])

print(mass,small_number,larger_number)
print(AA_dict_mass,mass_list)

#for i in range(small_number,larger_number):
#    while i>0:


#无法完成,要很长时间
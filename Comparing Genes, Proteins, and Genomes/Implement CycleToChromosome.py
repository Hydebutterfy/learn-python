def CycleToChromosome(Chromosome):
     Nodes=[]
     print(Chromosome)
     for j in range(int(len(Chromosome)/2)):
         if Chromosome[2*j]<Chromosome[2*j+1]:
             Nodes.append(int(Chromosome[2*j+1]/2))
         else:
             Nodes.append(-int(Chromosome[2*j]/2))

     print(Nodes)
     return Nodes


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement CycleToChromosome.txt') as input_data:
        perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())
    # map(): 1、对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。
    # lstrip, rstrip 去除左右两边的括号，

    # Get the list of recerals necessary to sort the given permutation.
    #print(list(perm))
    cycle_list = CycleToChromosome(list(perm))
    print(cycle_list)

    # Write the permutation in the desired form for in the desired output form for stepic.
    cycle =['(' + ' '.join([ ['', '+'][value > 0] + str(value) for value in cycle_list ])  +')'  ]

    # Print and save the answer.
    print(cycle)

    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement CycleToChromosome2.txt', 'w') as output_data:
        output_data.write('\n'.join(cycle))

if __name__ == '__main__':
    main()



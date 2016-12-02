

def CycleToChromosome(Chromosome):
    Nodes = []
    #print(Chromosome)
    for j in range(int(len(Chromosome)/2)):

        if int(Chromosome[2*j])<int(Chromosome[2*j+1]):

            Nodes.append(int(int(Chromosome[2*j+1])/2))

        else:
            Nodes.append(-int(int(Chromosome[2 * j])/2))

    #print(Nodes)
    return Nodes

def GraphToGenome(GenomeGraph):
    #print(GenomeGraph)
    P=[]
    l=len(GenomeGraph)
    #print(l)
    #起始的点
    Nodes = GenomeGraph[0]
    #起始点的起始值
    start_node=int(Nodes[0])
    #print(Nodes,start_node)


    for i in range(1,l):
        #print(GenomeGraph[i])
        #print(i)
        if Nodes==GenomeGraph[i]:
            continue

        #print()
        #判断是否取到头，尾减去头绝对值为1
        dif = abs(int(GenomeGraph[i][1])-start_node)
        #print(dif)
        if dif==1:
            #收集最后的点
            Nodes=Nodes+GenomeGraph[i]
            #print(Nodes)
            new_Nodes=[Nodes[-1]]+Nodes[0:-1]

            #print(new_Nodes)
            P.append(CycleToChromosome(new_Nodes))

            #判断是否结束
            if i==l-1:
                break
            else:
                #重新赋值
                Nodes=GenomeGraph[i+1]
                start_node=int(Nodes[0])

        else:
            Nodes=Nodes+GenomeGraph[i]
    return P



def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open(
            '/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement GraphToGenome.txt') as input_data:
        p = [input_data.read().strip().lstrip('(').rstrip(')').split('), (')]

    #print(p[0])
    Graph_p=[]

    for i in p[0]:
        Graph_p.append(i.split(", "))
    print(Graph_p)

    # Get the list of recerals necessary to sort the given permutation.
    cycle_list = GraphToGenome(Graph_p)

    print(cycle_list)
    cycle=''
    for i in cycle_list:
        cycle += '(' + ' '.join( ['', '+'][value > 0] + str(value)    for value in i )  + ')'

    print(cycle)

    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement GraphToGenome2.txt', 'w') as output_data:
        output_data.write(cycle)

if __name__ == '__main__':
    main()



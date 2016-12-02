



def ColoredEdges(P):
    Edges=[]
    for chromosome in P:
        print(chromosome)
        #print(chromosome.split())
        chromosome=list(map(int, chromosome.split() ))
        #print(chromosome)

        Nodes = ChromosomeToCycle(chromosome)
        Nodes.append(Nodes[0])
        print(Nodes)
        for j in range(int(len(chromosome))):
            Edges.append(tuple(Nodes[2*j+1:2*j+3]))

    print(Edges)

    return Edges




def ChromosomeToCycle(Chromosome):
    Nodes = []
    #print(Chromosome)
    for j in range(len(Chromosome)):
        i = Chromosome[j]
        if i > 0:
            Nodes.append(2 * i - 1)
            Nodes.append(2 * i)
        else:
            Nodes.append(-2 * i)
            Nodes.append(-2 * i - 1)
    return Nodes

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement ColoredEdges.txt') as input_data:
        p = [input_data.read().strip().lstrip('(').rstrip(')').split(')(')]

    print(p[0])
    coloredges=ColoredEdges(p[0])
    #ColoredEdges(p[0])
    print(coloredges)

    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement ColoredEdges2.txt', 'w') as output_data:
        output_data.write(str(coloredges))


if __name__ == '__main__':
    main()


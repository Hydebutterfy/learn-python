

def two_BreakOnGenomeGraph(GenomeGraph, i,I,j,J):
    GenomeGraph_new=[]
    for k in range(len(GenomeGraph)):
        if i==GenomeGraph[k][0]:
        #    GenomeGraph[k]=tuple([int(i),int(j)])
        #    j=0
            continue

        elif j==GenomeGraph[k][0]:
            #GenomeGraph[k]=tuple([int(j),int(i)])
            #i=0
            continue

        elif I == GenomeGraph[k][0]:
            #GenomeGraph[k]=tuple([int(I),int(J)])
            #J=0
            continue

        elif J == GenomeGraph[k][0]:
        #    GenomeGraph[k]=tuple([int(J),int(I)])
        #    I=0
            continue
        else:
            GenomeGraph_new.append(tuple([int(GenomeGraph[k][0]),int(GenomeGraph[k][1])]))

    GenomeGraph_new.append(tuple([int(i),int(j)]))
    GenomeGraph_new.append(tuple([int(I),int(J)]))


    return GenomeGraph_new


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement 2-BreakOnGenomeGraph.txt') as input_data:
        p = [input_data.read().strip().lstrip('(').rstrip(')').split('), (')]

    #print(p[0])
    Graph_p=[]
    for i in p[0]:
        Graph_p.append(i.split(", "))
    #print(Graph_p)

    colored_edges=input("replace colored edges:")
    i,I,j,J=colored_edges.split(", ")
    #print(i,I,j,J)

    GenomeGraph=two_BreakOnGenomeGraph(Graph_p,i,I,j,J)

    print(GenomeGraph)

    with open(
        '/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement 2-BreakOnGenomeGraph2.txt',
        'w') as output_data:
        output_data.write(str(GenomeGraph))

if __name__ == '__main__':
    main()

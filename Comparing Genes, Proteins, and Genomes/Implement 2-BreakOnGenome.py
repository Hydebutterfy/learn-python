
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

def ColoredEdges(P):
    Edges=[]
    for chromosome in P:
        #print(chromosome)
        #print(chromosome.split())
        chromosome=list(map(int, chromosome.split() ))
        #print(chromosome)

        Nodes = ChromosomeToCycle(chromosome)
        Nodes.append(Nodes[0])
        #print(Nodes)
        for j in range(int(len(chromosome))):
            Edges.append(tuple(Nodes[2*j+1:2*j+3]))

    #print(Edges)

    return Edges

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


def two_BreakOnGenomeGraph(GenomeGraph, i,I,j,J):
    #print(GenomeGraph)
    GenomeGraph_new=[]
    for k in range(len(GenomeGraph)):
        if GenomeGraph[k][0] not in (i,I,j,J):
            GenomeGraph_new.append(GenomeGraph[k])
    GenomeGraph_new.append(list([int(i),int(j)]))
    GenomeGraph_new.append(list([int(I),int(J)]))
    #加减edge

    order_temp_edge = [[],[]]
    for k in GenomeGraph_new:
        order_temp_edge[0].append(k[0])
        order_temp_edge[1].append(k[1])

    print(order_temp_edge)
    print(GenomeGraph_new)

    #重新排列edge的顺序
    #新的edge收集在GenomeGraph_order上
    GenomeGraph_order = []

    start_node = order_temp_edge[0][0]
    end_node=order_temp_edge[1][0]
    GenomeGraph_order.append(list([start_node, end_node]))
    del order_temp_edge[0][0]
    del order_temp_edge[1][0]

    #print(GenomeGraph_order)

    chromesome_start = start_node
    if (chromesome_start % 2) == 0:
        chromesome_stop = chromesome_start -1
    else:
        chromesome_stop = chromesome_start + 1

    #print(order_temp_edge,chromesome_start,chromesome_stop,start_node,end_node)

    while order_temp_edge!=[[],[]]:
        if (end_node % 2) == 0:
            start_node=end_node-1
        else:
            start_node = end_node +1

        #print(start_node)

        if start_node in order_temp_edge[0]:
            node_index = order_temp_edge[0].index(start_node)
            #print(node_index)
            end_node = order_temp_edge[1][node_index]
        else:
            node_index = order_temp_edge[1].index(start_node)
            #print(node_index)
            end_node = order_temp_edge[0][node_index]

        del order_temp_edge[0][node_index]
        del order_temp_edge[1][node_index]


        GenomeGraph_order.append(list([start_node, end_node]))

        #print(order_temp_edge,chromesome_start,chromesome_stop,start_node,end_node)

        if order_temp_edge !=[[],[]]:
            if chromesome_stop==end_node:
                start_node = order_temp_edge[0][0]
                end_node = order_temp_edge[1][0]
                GenomeGraph_order.append(list([start_node, end_node]))


                del order_temp_edge[0][0]
                del order_temp_edge[1][0]

                chromesome_start = start_node

                if (chromesome_start % 2) == 0:
                    chromesome_stop = chromesome_start - 1
                else:
                    chromesome_stop = chromesome_start + 1

            #print(GenomeGraph_order,order_temp_edge, chromesome_start, chromesome_stop, start_node, end_node)

    print(GenomeGraph_order)
    return GenomeGraph_order


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement 2-BreakOnGenome.txt') as input_data:
        c = [input_data.read().strip().lstrip('(').rstrip(')').split(')(')]


    #拿到的是序列，要变成ColoredEdges
    #print(p[0])
    coloredges=ColoredEdges(c[0])
    #print(coloredges)

    colored_edges = input("replace colored edges:")
    i, I, j, J = colored_edges.split(", ")
    # print(i,I,j,J)

    #修改断点位置
    GenomeGraph = two_BreakOnGenomeGraph(coloredges, int(i), int(I), int(j), int(J))
    print(GenomeGraph)

    #重新转换成数字序列
    cycle_list=GraphToGenome(GenomeGraph)

    print(cycle_list)
    cycle = ''
    for i in cycle_list:
        cycle += '(' + ' '.join(['', '+'][value > 0] + str(value) for value in i) + ')'

    print(cycle)

    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement 2-BreakOnGenome2.txt', 'w') as output_data:
       output_data.write(cycle)



if __name__ == '__main__':
    main()


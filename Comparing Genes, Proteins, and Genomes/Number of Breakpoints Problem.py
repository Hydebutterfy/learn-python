from operator import neg

def Number_of_Breakpoints_Problem(permutation):

    return sum( map(lambda x,y: x-y!=1, permutation+[len(permutation)+1], [0]+permutation)     )
    #相减，获得不等于1的次数
def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Number of Breakpoints Problem.txt') as input_data:
        perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())
    # map(): 1、对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。
    # lstrip, rstrip 去除左右两边的括号，
    #print(list(perm))
    # Get the list of recerals necessary to sort the given permutation.
    print(Number_of_Breakpoints_Problem(list(perm)))



if __name__ == '__main__':
    main()



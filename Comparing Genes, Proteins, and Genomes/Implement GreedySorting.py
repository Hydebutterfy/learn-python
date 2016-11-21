from operator import neg

def greedy_sorting(permutation):
    '''A greedy algorithm to sort by reversals.'''

    # Initialize a list to store all permutations in the transformation to the identity permutation.
    permutation_sequence = []

    # Lambda function to find the index of a given element in the permutation.
    k_index = lambda perm,k: list(map(abs, perm)).index(k)
    #lambda x:  x  建立函数，比def简单

    # Lambda function to swap and negate the region spanned from index i to index j.
    k_sort = lambda perm, i, j: perm[:i]+list(map(neg, perm[i:j+1][::-1])) + perm[j+1:]

    # Loop over the permutation to sort it, following the greedy sorting algorithm.
    i = 0
    while i < len(permutation):
        if permutation[i] == i+1:
            i += 1
        else:
            permutation = k_sort(permutation, i, k_index(permutation, i+1))
            permutation_sequence.append(permutation)

    # Note: the approximate reversal distance is the length of the permutation sequence.
    return permutation_sequence


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement GreedySorting.txt') as input_data:
        perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())
    # map(): 1、对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。
    # lstrip, rstrip 去除左右两边的括号，

    # Get the list of recerals necessary to sort the given permutation.
    reversal_list = greedy_sorting(list(perm))

    # Write the permutation in the desired form for in the desired output form for stepic.
    reversal_list = ['('+' '.join([['', '+'][value > 0] + str(value) for value in perm])+')' for perm in reversal_list]

    # Print and save the answer.
    print('\n'.join(reversal_list))

    with open('/Users/chenhaide/PycharmProjects/genome/Comparing Genes, Proteins, and Genomes/Implement GreedySorting2.txt', 'w') as output_data:
        output_data.write('\n'.join(reversal_list))

if __name__ == '__main__':
    main()



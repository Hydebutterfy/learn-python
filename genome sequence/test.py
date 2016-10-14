def new_dict_Cyclospectrum(Spectrum, M):
    l = len(Spectrum)
    # print(experimental_spectrum)
    new_experimental_spectrum = []
    for i in range(1, l):
        for j in range(i):
            item = Spectrum[i] - Spectrum[j]
            if item > 0:
                new_experimental_spectrum.append(str(item))

    new_experimental_spectrum = [int(x) for x in new_experimental_spectrum]
    print(new_experimental_spectrum)
    #print(' '.join(new_experimental_spectrum))

    temp_dict = {}
    for i in new_experimental_spectrum:
        if i not in temp_dict.keys() and i >= 57 and i < 200:
            Count_i = new_experimental_spectrum.count(i)
            temp_dict[i] = Count_i

    # print(temp_dict)
    order_score = sorted(temp_dict.values(), reverse=True)
    # print(order_score)
    M_count = order_score[M - 1]
    # print(M) 排名前20的数量

    dict_new_Cyclospectrum = {}
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z",
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

    position = 0
    for i in temp_dict:
        if temp_dict[i] >= M_count:
            dict_new_Cyclospectrum[alphabet[position]] = i
            position += 1

    # print(dict_new_Cyclospectrum)
    return dict_new_Cyclospectrum

Spectrum=[57,57,71,99,129,137,170,186,194,208,228,265,285,299,307,323,356,364,394,422,493]
M=20
print(new_dict_Cyclospectrum(Spectrum, M))
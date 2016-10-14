import re
def convolution_spectrum(Spectrum):
    l = len(Spectrum)
    # print(experimental_spectrum)

    new_experimental_spectrum=[]


    for i in range(1, l):
        for j in range(i):
            item = Spectrum[i] - Spectrum[j]
            if item > 0:
                new_experimental_spectrum.append(str(item))

    new_experimental_spectrum = [int(x) for x in new_experimental_spectrum]
    print(new_experimental_spectrum)
    #print(' '.join(new_experimental_spectrum))

    return new_experimental_spectrum



input_Spectrum = str(input("what is the Spectrum?"))
Spectrum = re.findall('\d+', input_Spectrum)
experimental_spectrum = [int(x) for x in Spectrum]
experimental_spectrum.sort()

print(experimental_spectrum)
print(convolution_spectrum(experimental_spectrum))
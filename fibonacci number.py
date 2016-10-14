__author__ = 'chenhaide'
n=int(input())
fibonaccinumber=[1,1]
if n>=3:
    for i in range(n-2):
        m=fibonaccinumber[len(fibonaccinumber)-1]+fibonaccinumber[len(fibonaccinumber)-2]
        fibonaccinumber.append(m)

print (fibonaccinumber)
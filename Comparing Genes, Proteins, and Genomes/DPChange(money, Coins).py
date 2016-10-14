import re

def DPChange(money, Coins):
    MinNumCoins={}
    MinNumCoins[0]=0
    for m in range(1,money+1):
        MinNumCoins[m]= float('inf')
        for i in range(len(Coins)):
            if m >= Coins[i]:
                if MinNumCoins[m-Coins[i]]+1<MinNumCoins[m]:
                    MinNumCoins[m]=MinNumCoins[m-Coins[i]]+1

    return MinNumCoins[money]


coins_1= str(input("what is the coins?"))
coins_2=re.findall('\d+', coins_1)
Coins=[int(x) for x in coins_2]

money=int(input("what is the money?"))
print(Coins,money)

print(DPChange(money, Coins))


#所有大小的都算出来,目标为终点。
#50,25,20,10,5,1
#40

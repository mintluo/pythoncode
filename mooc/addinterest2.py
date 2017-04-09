def addInterest(balance,rate):
    for i in range(len(balance)):
        balance[i] = balance[i]*(1+rate)
    #return newBalance
def test():
    amount = [1000,2000,3000,4000]
    rate = 0.05
    addInterest(amount, rate)
    print(amount)
test()

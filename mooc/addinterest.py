def addInterest(balance,rate):
    balance = balance*(1+rate)
    #return newBalance
def test():
    amount = 1000
    rate = 0.05
    addInterest(amount, rate)
    print(amount)
test()

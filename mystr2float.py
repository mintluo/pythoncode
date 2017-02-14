from functools import reduce

def str2float(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def fn(x,y):
        return 10*x+y
    zheng,feng=s.split('.')
    
    return reduce(fn,map(char2num,zheng))+reduce(fn,map(char2num,feng))*(0.1**len(feng))

print('str2float(\'123.456\')=',str2float('123.456'))

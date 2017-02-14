# -*- coding: utf-8 -*-
def num_iter():
    n=0
    while True:
        n=n+1
        yield n

def is_palindrome(n):
    m=int(str(n)[::-1])#倒序
    return m==n    

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))

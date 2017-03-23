# -*- coding: utf-8 -*-

def fact(n):
    '''

>>> fact(-1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    fact(-1)
  File "<pyshell#9>", line 3, in fact
    raise ValueError()
ValueError
>>> fact(0)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    fact(0)
  File "<pyshell#9>", line 3, in fact
    raise ValueError()
ValueError
>>> fact(1)
1
>>> fact(3)
6
>>> fact('a')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    fact('a')
  File "<pyshell#9>", line 2, in fact
    if n < 1:
TypeError: '<' not supported between instances of 'str' and 'int'

    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

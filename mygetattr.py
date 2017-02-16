# -*- coding: utf-8 -*-

class Chain(object):
    def __init__(self, path = 'a'):
        print("init......%s"%path)
        self._path = path
    def __getattr__(self, path):#在没有找到属性的情况下，才调用__getattr__
        print("getattr.......%s"%path)
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
    def __call__(self, users):
        print("call......%s"%users)
        return self.__getattr__(":"+users)

# test:
print(Chain().users('micheal').b.c)

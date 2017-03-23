# -*- coding: utf-8 -*-
import functools

def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*arg,**kw):
                print('begin call %s %s()'%(text,func.__name__))
                return [func(*arg,**kw),print('end call %s %s()'%(text,func.__name__))]
            return wrapper
        return decorator
    else:
        func=text
        @functools.wraps(func)
        def wrapper(*arg,**kw):
            print('begin call %s()'%(func.__name__))
            return [func(*arg,**kw),print('end call %s()'%(func.__name__))]
        return wrapper

@log
def now():
    print('time is now')

@log('try text')
def tomorrow():
    print('time is tomorrow')

now()

tomorrow()

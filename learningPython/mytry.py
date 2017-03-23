# -*- coding: utf-8 -*-
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('a')#bar('0')
    except Exception as e:#捕获除与程序退出sys.exit()相关之外的所有异常
        #print('Error:', e)
        logging.exception(e)#程序打印完错误信息后会继续执行，并正常退出
    finally:
        print('finally...')

'''try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
    
finally:#可以没有finally语句
    print('finally...')
print('END')'''

# test:
main()
print('END')

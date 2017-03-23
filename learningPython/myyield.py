def f():
    print('first')

    a = yield 1  #函数包含了yield，这意味着这个函数是一个Generator，下面用next()调用时将None传给a①  
    print(a)
    print('second')
    
    b = yield 2 #2这个值只是迭代值，调用next时候返回的值。
    print(b)
    print('third')
    
    c = yield 3	    
    print(c)
    print('fourth')
    
    d = yield 4	    
    print(d)

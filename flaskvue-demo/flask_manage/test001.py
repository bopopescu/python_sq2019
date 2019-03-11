# -*- coding: utf-8 -*-

# @Time    : 2018/12/6 14:26
# @Author  : songq001
# @Comment : 



# def aaa(a, b):
#     return b, a
#
#
# c, d = aaa(2, 1)
# print(c, d)

# print(int(float('12.55')))

# def bbb(x, n):
#     a = 1
#     while n > 0:
#         n = n-1
#         a = a*x
#     return a
#
#
# print("x=")
# x = float(input())
# x = int(x)
# print("n=")
# n = float(input())
# n = int(n)
# print(bbb(x, n))
#
# print(bbb(2, 2))


# 闭包
def outer(x):
     def inner():
         print("Inside inner" + "_" + x)
     return inner

foo = outer("aaaa111")
print(foo)
foo()       # 等同于 outer("aaaa111")()

print("\n" + "#################################################################")

# 装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print ('2013-12-25')

now()


print("\n" + "#################################################################")

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')                         # 等同 now = log('execute')(now)
def now():
    print('2013-12-25')

now()

print(now.__name__)    # __name__已经从原来的'now'变成了'wrapper'，因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
                       # 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：


import functools

def log(func):
    @functools.wraps(func)                          # 只需记住在定义wrapper()的前面加上@functools.wraps(func)即可
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 或者针对带参数的decorator：
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print ('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


####################################################################################
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
# 又支持：
@log('execute')
def f():
    pass
####################################################################################

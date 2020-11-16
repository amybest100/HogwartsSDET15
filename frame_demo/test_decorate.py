# 原始a函数
def a():
    print("a")


# 加强a函数方法一：直接修改原函数
# def a():
#     print("before")
#     print("a")
#     print("after")

# 加强a函数方法二：编写一个函数对a函数进行加强
def enhance(func):
    print("before")
    func()
    print("after")


def test_a():
    enhance(a)


# 加强a函数方法三：使用装饰器（步骤：定义一个函数，传参是想要加强的函数
def tmp(func):
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")

    return wrapper


@tmp
def a1():
    print("a1")


def test_a1():
    a1()

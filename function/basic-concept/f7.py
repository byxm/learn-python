# 函数作用域


def demo():
    c = 10
    for i in range(0, 10): # python不像Javascript有块级作用域的概念
        d = i
        e = 10
    print(d, e)

demo()
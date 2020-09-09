# 可变参数，可以将传入的参数指定为可变参数，这样传入的参数可以多个，接收参数可以一个


def demo(first,*param):
    print(first)
    print(param)



demo(1,2,3,4,5,6,7)


def squsum(*param):
    sumResult = 0
    for s in param:
        sumResult = sumResult + s * s

    return sumResult

print(squsum(1,2))


def showWeather(**param):     # 两个**的可变参数能够支持关键字参数
    print('paraass', param)
    for key,value in param.items(): # 遍历关键字参数字典键值需要使用items
        print('city:' + key, 'weather:' + value)

# showWeather(sc = '多云', xz = '晴天', hb = '暴雨')

m = {'sc':'热能', 'zx':'很热'}
showWeather(**m)

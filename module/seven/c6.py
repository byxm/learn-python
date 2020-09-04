import newModule



print(newModule.sys.path)


# 模块和包是不会重复导入的，在多个地方导入相同的包但是只会执行一次
# 避免循环导入包
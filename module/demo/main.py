# 入口文件没有顶级包


import package2.package4.m2 # 绝对路径引入,入口文件不支持相对导入

print(__name__) # 入口文件会把__name__默认设置为__main__而不是文件名，所以不能在入口文件里面使用相对路径导入
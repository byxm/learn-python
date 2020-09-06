import newModule.c7

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~C15~~~~~~~~~~~~~~~~~~~~~~~~')
print('package: ' + (__package__ or '当前模块不属于任何包')) # 入口文件也不属于任何包
print('name: ' + __name__)  # 入口文件的名称是 __main__
print('doc: ' + (__doc__ or '当前模块没有任何文档'))
print('file: ' + __file__) # file 的值取决于python脚本执行输入参数的值


'''
对于python的入口文件来说都没有包，即便是有声明__init__.py文件也不行
'''
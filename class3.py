# _*_ coding: utf-8 _*_
# @Time: 2021-10-26 16:14
# Author: Gruaa

# 创建类 MyClass
class MyClass:
    # 创建属性 name，值为 Sam
    def __init__(self,name):
        self.name=name
        name = "Sam"
    # 创建方法 sayHi
    def  sayHi(self):
        print('Hello %s' % self.name)

# 创建一个 MyClass 的对象
mc = MyClass("Sam")

# 输出 mc 的 name 属性
print(mc.name)

# 调用 mc 的 sayHi 方法
mc.sayHi()
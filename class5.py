# _*_ coding: utf-8 _*_
# @Time: 2021-10-26 16:32
# Author: Gruaa

class Pen:
    name = 'Pen'
    def __init__(self,name):
        self.name=name

    def write(self):
        print('I have a', self.name)

# 创建两个 Pen 子类，并修改各自的 name
# 一个叫 ApplePen
class ApplePen(Pen):
    name = 'ApplePen'

# 一个叫 PineapplePen
class PineapplePen(Pen):
    name = 'PineapplePen'

# 分别创建这两个子类的对象
ap = Pen('ApplePen')
pp = Pen('PineapplePen')

ap.write()
pp.write()
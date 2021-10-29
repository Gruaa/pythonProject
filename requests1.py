# _*_ coding: utf-8 _*_
# @Time: 2021-10-26 15:13
# Author: Gruaa

class GuoJia_JiangPai:
    def __init__(self,country,jin,yin,tong):
        self.country = country
        self.jin = jin
        self.yin = yin
        self.tong = tong
    def XinZeng_JiangPai(self,mingci):
        if mingci == 1:
            self.jin+=1
        elif mingci ==2:
            self.yin+=1
        elif mingci ==3:
            self.tong+=1
    def count(self):
        return (self.jin + self.yin + self.tong)
    def __str__(self):
        return "%s\t金牌%d\t银牌%d\t铜牌%d\t总数%d" % (self.country,self.jin,self.yin,self.tong,self.count())

ZhongGuo = GuoJia_JiangPai('中国',4,0,0)
MeiGuo = GuoJia_JiangPai('美国',2,2,5)
YingGuo = GuoJia_JiangPai('英国',3,8,1)

ZhongGuo.XinZeng_JiangPai(1)
MeiGuo.XinZeng_JiangPai(2)
list = [ZhongGuo,MeiGuo,YingGuo]
listJin = sorted(list,key=lambda x:x.jin,reverse=True)
for i in listJin:
    print(i)
print('-')
listCount = sorted(list,key=lambda x:x.count(),reverse=True)
for i in listCount:
    print(i)
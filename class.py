class dog:
    def __init__(self,name,high,blood,power):#属性，要有参数，调用属性不需要（），如print（d1.name）
        self.name=name
        self.high=high
        self.blood=blood
        self.power=power

    def bark(self):#方法，调用方法需要（），如d1.bark（）
        print(f"我是{self.name},我身高{self.high},我的血量是{self.blood},我的攻击力是{self.power}")

    def attck(self,dog2):
        dog2.blood=dog2.blood-self.power

    def reduce_blood(self,reduce_value):
        if reduce_value >self.blood:
            self.blood=0
        else:
            self.blood=self.blood-reduce_value


d1=dog("大黄",0.7,10,1)
d2=dog("小黑",0.5,10,2)

print(d2.name)


d2.bark()
d1.attck(d2)
d2.reduce_blood(4)
d2.reduce_blood(4)
d2.reduce_blood(4)
d2.bark()




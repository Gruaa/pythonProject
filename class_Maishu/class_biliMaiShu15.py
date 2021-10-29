class Dog:

    def __init__(self,name,height,power):
        self.name=name
        self.height=height
        self.power=power
        self.blood = 10


    def bark(self):
        print(f"我是{self.name},我身高{self.height},我的血量是{self.blood},我的攻击力是{self.power}")

#牧羊犬（有number_of_sheeps属性，有protect（）方法）
class SheepDog(Dog):
    def __init__(self,name,height,power,number_of_sheeps):
        super().__init__(name,height,power)
        self.number_of_sheeps = number_of_sheeps
    def protect(self):
        print("我开始保护小羊了！！")
    def bark(self):#子类有方法，同名的优先使用子类的方法。
        print("我是牧羊犬，我骄傲")
        super().bark()#调用父类中的方法

#警犬(有ability属性，有detect（）方法）
class PoliceDog(Dog):
    def __init__(self,name,height,power,ability):
        super().__init__(name,height,power)
        self.ability = ability
    def detect(self):
        print("我可以做侦查工作！！")


#宠物犬（有price属性，有sing（）方法）
class PetDog(Dog):
    def __init__(self,name,height,power,price):
        super().__init__(name,height,power)
        self.price = price
    def sing(self):
        print("我来给你唱只歌吗？？")


# sd = SheepDog('牧羊犬1号',0.6,4,5)
# print(sd.name)
# print((sd.blood))
# sd.bark()
#
# pd = PoliceDog("警犬一号",0.6,5,"抓坏人")
# print(pd.ability)
# pd.bark()
#
# sd.protect()
# #pd.protect()别的狗无法调用子类的属性
# pd.detect()
#
# sd.bark()
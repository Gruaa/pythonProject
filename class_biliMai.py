class dog:
    dogs = []#用来保存所有狗的列表

    @classmethod
    def number_of_dogs(cls):
        return len(cls.dogs)

    # number_of_dogs = 0 #类属性。要变所有的实例都会变，通过类名访问，如：dog.number_of_dogs
    def __init__(self,name,high,blood,power):#实例属性，要有参数，调用属性不需要（），如print（d1.name）
        self.name=name
        self.high=high
        self.blood=10
        self.power=power
        dog.dogs.append(self)#添加狗
        # dog.number_of_dogs = dog.number_of_dogs + 1#每创建一个实例，增加一个计数

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


# print(dog.number_of_dogs)# 通过类名访问类属性
# # print（dog.self.name)#不能通过类名访问实例的属性
# print(d1.number_of_dogs)#通过实例访问类属性，

# dog.number_of_dogs = 8#通过类名访问并修改类属性
# print(dog.number_of_dogs)
# print(d1.number_of_dogs)
# print(d2.number_of_dogs)
#
# d1.number_of_dogs = 5 #通过实例访问并修改类属性，只能修改对应的实例自己的改属性。
# # 给d1添加了一个实例属性,实例属性和类属性名字相同时，访问实例优先访问实例属性
# print(dog.number_of_dogs)
# print(d1.number_of_dogs)
# print(d2.number_of_dogs)

# for a in dog.dogs:
#     print(a)
# print(dog.dogs)

print(dog.number_of_dogs())
print(d1.number_of_dogs())
print(d2.number_of_dogs())
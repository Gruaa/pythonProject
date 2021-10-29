
class Car:

    def __init__(self,name,brand,number_of_people,max_people):
        self.name=name
        self.brand=brand
        self.number_of_people = 0
        self.max_people=max_people

    def run(self):
        print(f"{self.name} is running!")

    def set_people(self,number):
        if self.max_people >= number >= self.number_of_people:
            self.number_of_people=number
        else:
            print("初始人数设置错误")


    def increase_people(self):
        if self.number_of_people<self.max_people:
            self.number_of_people+=1
        else:
            print("人满，无法上车")

    def reduce_people(self):
        if self.number_of_people>=1:
            self.number_of_people-=1
        else:
            print("人空!")
    def show(self):
        print(f"My name is {self.name},My brand is {self.brand},There have now {self.number_of_people} people,"
              f"There can seat {self.max_people} people.")


Car1=Car("君威","别克",3,5)
# Car2=Car("宋PLUS","比亚迪")
# Car1.show()
# Car2.show()
# Car1.run()
Car1.show()
Car1.set_people(2)
Car1.show()
Car1.increase_people()
Car1.show()
Car1.increase_people()
Car1.show()
Car1.increase_people()
Car1.show()
Car1.increase_people()
Car1.show()

Car1.reduce_people()
Car1.show()
Car1.reduce_people()
Car1.show()
Car1.reduce_people()
Car1.show()
Car1.reduce_people()
Car1.show()
Car1.reduce_people()
Car1.show()
Car1.reduce_people()
Car1.show()



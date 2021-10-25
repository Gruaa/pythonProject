
class Car:

    def __init__(self,name,brand,number_of_people,max_people):
        self.name=name
        self.brand=brand
        self.max_people=max_people
        self.number_of_people = 0

    def show(self):
        print(f"My name is {self.name},My brand is {self.brand},I have now {self.number_of_people} people")

    def run(self):
        print(f"{self.name} is running!")

    def set_people(self,x):
        number_of_people=x

    def increase_people(self):
        if number_of_people<=max_people:
            number_of_people+=1
        else:
            print("客满，无法上车")

    def reduce_people(self):
        number_of_people-=1


Car1=Car("君威","别克",0,5)
# Car2=Car("宋PLUS","比亚迪")
# Car1.show()
# Car2.show()
# Car1.run()


Car1.show()
Car1.set_people(1)
Car1.show()

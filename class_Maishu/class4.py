# _*_ coding: utf-8 _*_
# @Time: 2021-10-26 16:26
# Author: Gruaa

class car:
    speed = 0
    def drive(self,distance):
        time = distance / self.speed
        print(time)


car1=car()
car1.speed= 60
car1.drive(100)

car2=car()
car2.speed=10
car2.drive(200)

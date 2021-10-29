# _*_ coding: utf-8 _*_
# @Time: 2021-10-29 15:08
# Author: Gruaa

class Medals:

    def __init__(self,country_name,number_of_gold,number_of_silver,number_of_copper):
        self.country_name = country_name
        self.number_of_gold = number_of_gold
        self.number_of_silver = number_of_silver
        self.number_of_copper = number_of_copper

    def increase_gold_medals(self,a):
        a = int(input("Please enter how many gold MEDALS?"))
        self.number_of_gold = self.number_of_gold + a

    def tm(self):
        return (self.number_of_gold + self.number_of_silver + self.number_of_copper)#

    def prints(self):
        print(f"{self.country_name} have {self.number_of_gold} gold medals,{self.number_of_silver} silver medals,"
              f"{self.number_of_copper} copper medals.{self.country_name} have {tm} medals!")

    def __str__(self):
        return "(%s,%s,%s,%s)" % (self.country_name,self.number_of_gold,self.number_of_silver,self.number_of_copper)

c1 = Medals("China",100,99,80)
c2 = Medals("USA",80,70,60)
c3 = Medals("Japan",9,3,300)

list = [c1,c2,c3]

list_gold = sorted(list,key=lambda x:x.number_of_gold,reverse=True)#
for i in list_gold:
    print(i)

list_total = sorted(list,key= lambda x:x.tm(),reverse=True)#
for j in list_total:
    print(j)
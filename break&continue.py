# i = 0
# while i < 5:
#    i += 1
#    for j in range(3):
#        print ("j",j)
#        if j == 2:
#            print('这里break了')
#            break
#    for k in range(3):
#        if k == 2:
#            print('这里continue了')
#            continue
#        print ("K",k)
#    if i > 3:
#        print('这里ibreak了')
#        break
#    print ("i",i)


# 1,2,3,4 四个数字，能组成多少个互不相同且无重复数字的三位数？分别是多少？
# 要求：输出 1,2,3,4 组合出的所有无重复数字的三位数。

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=k and k!=j and i!=j:
#                 print(i*100+j*10+k)


# BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字
# BMI < 18.5 体重偏轻
# 18.5 <= BMI < 24 体重正常
# BMI >= 24 体重偏重
# 设计一个BMI计算器吧，看看自己体重是否正常。
# 输入：身高、体重值
# 输出：BMI 指数、是否正常

# w=float(input("请输入体重（公斤）"))
# h=float(input("请输入身高（米）"))
# bmi=float(w/(h**2))
# print("你的bmi是：%.2f"%bmi)
# if bmi<18.5:
#     print("体重偏轻")
# elif 18.5<=bmi<=24:
#     print("体重正常")
# else:
#     print("体重偏重")


# 通过 from random import * 引入 random 模块后，调用其内部的方法 randint()，正确的调用写法是randint(-3,0)


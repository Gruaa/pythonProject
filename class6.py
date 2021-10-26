# _*_ coding: utf-8 _*_
# @Time: 2021-10-26 16:45
# Author: Gruaa


# 【问题描述】
# 奥运会期间，奖牌榜备受关注。奖牌榜上的信息每天都在更新。
#
# 要求：运用面向对象的知识，构造一个类来描述每个国家的奖牌情况。
# 类的属性包括：国家名、金/银/铜牌数量
# 再提供方法：新增奖牌、输出奖牌榜信息、获取奖牌总数等
#
# 然后创建几个国家的奖牌数据，分别按金牌数和奖牌总数对奖牌榜列表进行排序

class medals:
    def __init__(self,country_name,gold_number,silver_number,copper_number,total_number):
        self.country_name=country_name
        self.gold_number=gold_number
        self.silver_number=silver_number
        self.copper_number=copper_number
        self.total_number=total_number

    def increa
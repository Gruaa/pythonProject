# _*_ coding: utf-8 _*_
# @Time: 2021-10-26 15:29
# Author: Gruaa

import re
text= "I am ShiryHinton,I am his wife."
# m = re.findall(r"hi", text)#匹配所有包含“hi”
# m = re.findall(r"\bhi\b",text)#仅匹配“hi”这个单词，开头和结尾都没有
# m = re.findall(r"[hi]",text)#匹配所有的“h“，”i“
m = re.findall(r"[Hh]i",text)#匹配了“Hi”和“hi”
if m:
    print(m)
else:
    print('no match')
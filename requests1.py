# _*_ coding: utf-8 _*_
# @Time: 2021-10-26 15:13
# Author: Gruaa

import requests
r = requests.get("http://httpbin.org/get")

print(r.text)
print(r.status_code)
print(r.encoding)
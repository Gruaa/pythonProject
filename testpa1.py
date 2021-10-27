import requests
#指定url
url="https://uland.taobao.com/"
#发送请求get(url, params=None, **kwargs)
response=requests.get(url=url,)
#转成文本数据
page_text=response.text
#打印出文本
print(page_text)

#存储数据
#只写打开文件，输入文本类型为utf-8
fp=open(file="./sou_gou_shu_ju.html",mode='w',encoding="utf-8")
#文本写入
fp.write(page_text)
fp.close()
print("爬爬爬over")
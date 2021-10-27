import requests
url="https://www.baidu.com/s?"
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/25"
}
kw=input("想搜索啥子呢？")
param={
"wd":kw,
}

#headers参数填入身份标识
response=requests.get(url=url
,params=param
,headers=header
)
page_text=response.text
print(page_text)
#根据搜索内容确定保存文件名称file_name
file_name=kw+".html"
fp = open(file=file_name,mode='w+',encoding="utf-8")
fp.write(page_text)
fp.close()
print("爬爬爬over")

print(response)


# 咕咕机SDK guguji_sdk
为了更好的使用咕咕机，方便调用相关api接口。

特地制作了一个咕咕机sdk



# 依赖环境  Dependent environment

```
pip intsall httpx
```
[https://www.python-httpx.org/](https://www.python-httpx.org/)

请使用 python 3.8.x 并安装httpx 




# 引用并创建对象
```
from guguji_sdk import gusdk #

guguji=gusdk(ak='',memobirdID='')
```
在引用对象中输入ak和memobirdID 
ak通过邮件和官方获得 
memobirdID双击咕咕机获得 





# 打印文本 print_text
```
guguji.print_text_paper('我的咕咕机')
```




# 打印图片 print_photo
```
guguji.print_photo_paper('p.png')
```
导入图片文件路径，支持jpg和png





# 打印网页 通过Url print_url
```
url='http://open.memobird.cn/Home/testview'
guguji.print_url(url)
```



# 打印网页 通过html  print_html  
```
with open('gu.html',encoding = "utf-8") as f:
    html = f.read()
print(html)

#guguji.print_html(html)
```





# 获取打印状态  get_status
```
guguji.get_status(printcontentID) #44182537
```
printcontentID 从前面各类打印方法返回

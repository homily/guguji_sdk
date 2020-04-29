

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
html="""
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Memobird 开放平台</title>
</head>
<body>
<h1 class="text-danger">错误。</h1>
<h2 class="text-danger">处理你的请求时出错。</h2>
        <div class="foot">
            <a target="_blank" href="http://www.memobird.cn/" style="text-decoration: none;color:#ffffff">关于memobird</a>;
            Copyright 2015 Intretech. All Rights Reserved.
        </div>
    </div>
</body>
</html>
"""
url='http://open.memobird.cn/Home/testview'



guguji.print_html(html)
```





# 获取打印状态  get_status
```
resp=guguji.get_status(44182537)
```

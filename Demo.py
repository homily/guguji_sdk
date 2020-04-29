from guguji_sdk import gusdk

#
guguji=gusdk(
    ak='Your accesskey', #access key
    memobirdID='Your memobirdID' #咕咕机的设备编号(双击设备吐出来的设备编号) From double click memobird
    )

#打印文本 print_Text
guguji.print_text_paper('我的咕咕机')

#打印图片 print_photo
guguji.print_photo_paper('p.png') #png  or  jpg

#获取打印状态 get_status
guguji.get_status(printcontentID) #44182537

#打印网页 print_url
url='http://open.memobird.cn/Home/testview'
guguji.print_url(url)

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

#打印html标记语言 print_html
guguji.print_html(html)

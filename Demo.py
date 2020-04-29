from guguji_sdk import gusdk

guguji=gusdk(
    ak='Your APIKey',
    memobirdID='Your memobirdID'
    )

guguji.print_text_paper('我的咕咕机')
guguji.print_photo_paper('p.png')
resp=guguji.get_status(44182537)
res=guguji.print_url('http://open.memobird.cn/Home/testview')

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
guguji.print_html(html)

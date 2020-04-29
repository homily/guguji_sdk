import httpx
import time
import base64



class gugu_sdk:

    def __init__(self,ak,memobirdID):
        self.ak=ak
        self.memobirdID=memobirdID
        self.host='http://open.memobird.cn'

    def _get(self,url,params={}):
        self.timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.params_sys = {'ak': self.ak,'timestamp':self.timestamp}
        self.params={**params, **self.params_sys}
        #print(self.params)
        return self._request('GET', path=url, params=params)


    def _post(self,url,params={}):
        self.timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.params_sys = {'ak': self.ak,'timestamp':self.timestamp}
        self.params={**params, **self.params_sys}
        pprint.pp(self.params)
        return self._request('POST', path=url, params=params)
    
    def _request(self, method: str, path: str, **kwargs):
        try:
            if method=='GET':
                response=httpx.get(path, params=self.params)
            if method=='POST':
                response=httpx.post(path, data=self.params)
            return (response.json())
        except:
            print(response.text)

    def _base64str(self,raw):
        
        if type(raw)==str:raw=bytes(raw,encoding='gb18030')
        base64_data = base64.b64encode(raw)
        self.base64_str = base64_data.decode()
        return (self.base64_str)
       
    def get_ak(self)-> None:
        url = f'{self.host}/home/setuserbind'
        params={
              'memobirdID':self.memobirdID,
              'useridentifying':'146688',
              }
        return (self._get(url,params))
        

    def print_text_paper(self,text):
        url = f'{self.host}/home/printpaper'
        str_encrypt=text
        base64_encrypt=self._base64str(text)
        printcontent=(f"T:{base64_encrypt}")
        userID=guguji.get_ak()['showapi_userid']
        params = {
              'printcontent':printcontent,
              'memobirdID':self.memobirdID,
              'userID':userID
              }
        return (self._post(url,params))
        
    def print_photo_paper(self,photo):
        url = f'{self.host}/home/printpaper'
        base64photo=self.get_signalbase64pic(photo)['result']
        printcontent=(f'P:{base64photo}')
        userID=guguji.get_ak()['showapi_userid']
        params = {
              'printcontent':printcontent,
              'memobirdID':self.memobirdID,
              'userID':userID
              }
        return (self._post(url,params))


    def get_status(self,printcontentid):
        url = f'{self.host}/home/getprintstatus'
        self.printcontentid=printcontentid
        params = {
              'printcontentid':self.printcontentid,
              }
        return (self._post(url,params))


    def get_signalbase64pic(self,imgBase64String):
        url = f'{self.host}/home/getSignalBase64Pic'
        with open(imgBase64String, 'rb') as f:
            self.imgBase64String=self._base64str(f.read())
        params = {
              'imgBase64String':self.imgBase64String,
              }
        return (self._post(url,params))

    def print_url(self,PrintUrl):
        url = f'{self.host}/home/printpaperFromUrl'
        self.printUrl=PrintUrl
        userID=guguji.get_ak()['showapi_userid']
        params = {
              'printUrl':self.printUrl,
              'memobirdID':self.memobirdID,
              'userID':userID
              }
        return (self._post(url,params))

    def print_html(self,PrintHtml):
        url = f'{self.host}/home/printpaperFromHtml'
        self.printHtml=self._base64str(PrintHtml)
        print(self.printHtml)
        userID=guguji.get_ak()['showapi_userid']
        params = {
              'printHtml':self.printHtml,
              'memobirdID':self.memobirdID,
              'userID':userID
              }
        return (self._post(url,params))

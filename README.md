# login_github_by_three_methods



>使用scrapy和selenium登陆github的三种方法<br>

>>*1.手动登陆之后复制cookies,使用scrapy里的Request方法实现登陆<br>
  *2.正常抓包,使用scrapy里的FormRequest方法发送post请求登陆<br>
  *3.先使用selenium自动登陆获取cookies,处理cookies,再使用scrapy里的Request方法登陆


>主要方法文件为spiders里面的:<br>
>>1.login_direct.py<br>
  2.login_FormReq.py<br>
  3.login_selenium.py

>主要思路:<br>
>>方法1:<br>
>>>1.手动登陆github,来到https://github.com/用户名
   (这也是验证登陆是否成功的地址)<br>
   2.复制cookies(字符串,不能直接使用),再用字典推导式组建成需要的cookies<br>
   3.使用scrapy.Request()方法携带cookies对验证地址发送get请求,打印响应的title标签的内容,如果是你的用户名,则表明登陆成功

>>方法2:<br>
>>>1.抓包比对完之后发现登陆是对 https://github.com/session 发起post请求<br>
   2.其中formdata中有四个动态的值:authenticity_token ;required_field_3054(后面四个字符变化) ; timestamp_secret ;timestamp<br>
   3.比对发现,四个值均可对登陆网页 (https://github.com/login) 提前发起请求获取,所以将此作为起始url<br>
   4.解析响应组建需要的formdata字典<br>
   5.使用scrapy.FormRequest()方法携带cookies对验证地址发送post请求<br>
   6.最后验证

>>方法3:<br>
>>>1.使用selenium提前获取登陆之后的cookies<br>
   2.处理cookies:temp_list = self.driver.get_cookies();;;cookies = {dict['name']: dict['value'] for dict in temp_list}<br>
   3.再在scrapy登陆时传入cookies参数即可<br>
   4.最后验证
   
>遇到的问题:<br>
>>scrapy自动过滤掉重复的url,即不重复发请求

  (但是github登陆时要对github.com/login请求两次:第一次是提前获取数据,第二次是被重定向到login)
  
  url变化过程:login --> session --> login-->github.com(登陆后的主页) --> github.com/yourname(个人主页)
  
>>解决:<br>

 >>对 https://github.com/login 请求时添加参数dont_filter=True
    





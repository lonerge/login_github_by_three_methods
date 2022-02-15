import scrapy


# 登录github第二种方法，FormRequest携带data参数登录:
        # 1.抓包比对完之后发现登陆是对https://github.com/session发起post请求
        # 2.其中formdata中有四个动态的值:authenticity_token ;required_field_3054(后面四个字符变化) ; timestamp_secret ;timestamp
        # 3.比对发现,四个值均可对登陆网页(https://github.com/login)提前发起请求获取,所以将此作为起始url

        # 遇到的问题:scrapy自动过滤掉重复的url,即不重复发请求
        # (但是github登陆时要对github.com/login请求两次:第一次是提前获取数据,第二次是被重定向到login)
        # url变化过程:login --> session --> login-->github.com(登陆后的主页) --> github.com/yourname(个人主页)



class LoginFormreqSpider(scrapy.Spider):
    name = 'login-FormReq'
    allowed_domains = ['github.com']
    # start_urls = ['https://github.com/login']

    def start_requests(self):
        # 1.对登陆页面发送请求获取响应
        url = 'https://github.com/login'
        # headers = {
        #     # 'referer': 'https://github.com'
        #     'referer': 'https://github.com/login'
        #
        #
        # }
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # pass
        # 解析响应,提取四个动态的data,再组建FormRequest对象并返回
        token = response.xpath('//*[@id="login"]/div[4]/form/input[1]/@value').extract_first()
        require = response.xpath('//*[@id="login"]/div[4]/form/div/input[9]/@name').extract_first()
        time = response.xpath('//*[@id="login"]/div[4]/form/div/input[10]/@value').extract_first()
        time_secret = response.xpath('//*[@id="login"]/div[4]/form/div/input[11]/@value').extract_first()
        formdata = {
            'commit': 'Sign in',
            'authenticity_token': token,
            'login': '2726750297@qq.com',
            'password': '2726750297@Dl',
            'trusted_device': '',
            'webauthn-support': 'supported',
            'webauthn-iuvpaa-support': 'unsupported',
            'return_to': 'https://github.com/login',
            'allow_signup': '',
            'client_id': '',
            'integration': '',
            require: '',
            'timestamp': time,
            'timestamp_secret': time_secret

        }
        print(formdata)
        # headers = {
        #     'referer': 'https://github.com/login'
        # }
        yield scrapy.FormRequest(url="https://github.com/session", formdata=formdata, callback=self.after_login)

    # def add(self, response):
    #     yield scrapy.Request(url='https://github.com/login', callback=self.after_login)

    def after_login(self, response):
        print("after...")
        # 对主页地址发起请求,为验证做准备
        yield scrapy.Request(url="https://github.com/lonerge", callback=self.verify)

    def verify(self, response):
        print("verify...")
        # 登陆之后进行验证:
        title = response.xpath('/html/head/title/text()').extract_first()
        print(title)




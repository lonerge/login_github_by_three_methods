import scrapy
from selenium import webdriver




# 第三种方法: 使用selenium提前获取登陆之后的cookies, 再在scrapy登陆时传入cookies参数即可



class LoginSeleniumSpider(scrapy.Spider):
    name = 'login_selenium'
    allowed_domains = ['github.com']
    # start_urls = ['https://github.com/login']
    opt = webdriver.ChromeOptions()
    opt.add_argument('--headless')
    opt.add_argument('--gpu-disable')
    driver = webdriver.Chrome(chrome_options=opt)

    def start_requests(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'referer': 'https://github.com'
        }
        cookies = self.get_cookies()
        yield scrapy.Request(url='https://github.com/lonerge', headers=headers, cookies=cookies, callback=self.parse, dont_filter=True)

    def get_cookies(self):
        # 1.提前使用selenium模块获取登陆之后的cookies,为后续scrapy登陆做准备
        self.driver.get(url='https://github.com/login')
        self.driver.find_element(by='xpath', value='//*[@id="login_field"]').send_keys('lonerge')
        self.driver.find_element(by='xpath', value='//*[@id="password"]').send_keys('2726750297@Dl')
        self.driver.find_element(by='xpath', value='//*[@id="login"]/div[4]/form/div/input[12]').click()
        self.driver.get(url='https://github.com/lonerge')
        logined = self.driver.current_url
        print(logined)
        cookies = {}
        if logined == "https://github.com/lonerge":
            temp_list = self.driver.get_cookies()
            cookies = {dict['name']: dict['value'] for dict in temp_list}
            return cookies

    def parse(self, response):
        title = response.xpath('/html/head/title/text()').extract_first()
        print(title)
        if title == "lonerge":
            print(f'{title}:登陆成功...')






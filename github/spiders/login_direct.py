import scrapy


class LoginDirectSpider(scrapy.Spider):
    name = 'login-direct'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/lonerge']

    def start_requests(self):
        url = self.start_urls[0]
        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            # 'referer': 'https://github.com/session'
        }
        temp = '_octo=GH1.1.1577477150.1644808892; tz=Asia%2FShanghai; _device_id=7a6bb5b287034210b152b566b1d4ffb6; has_recent_activity=1; user_session=sM9n0kwMGgL1KY89E9xS4dPdMXrPD0LUvelJKsg1dz93O9bx; __Host-user_session_same_site=sM9n0kwMGgL1KY89E9xS4dPdMXrPD0LUvelJKsg1dz93O9bx; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=lonerge; _gh_sess=8oogk0uvTkJzsQZnbAHhejYOnLn6XWe7t45DCMDVm0WZVG1vqyEcoe9LshsFXn8Yg%2Fpz%2BFowrSWOauAI9%2BbfBpr%2FDx%2BP0odKwrlMNeNVZrguDWw%2FfaOuopqAclSpr6lOZ7JEDc%2FgcLv6%2FA5Nhwp63lzMk7q92RI0v1obZxCh5qBfTPLz5jh48tC%2ByuemMRpQ29o7qAoND7uT1HJFNYDWG81gYYjfBvx7IXQOop9vM%2BbLw3%2F7OQcGM6yAgg2vFseGQ%2FR2zGc5QlaGnLZOJHF4xCnSe0ErYRswj93vVjtdzsylitbDjVaiN8x%2BuBzoVDZLXPFbyY4NZcwpF%2FQszKmK%2F3alVPpidcQ8ppncAWmqZxuKBxU6WhMvyNY7F29CAkVC70V%2FCXH%2BxlCqZq7niHb5V%2F9Eyr99VBgy0JBbB2CuPfV%2BKAAr%2Fu6cyhAxYmBapDLmVt9UmBShHU42HPlm6x46ddo9yaquktpMYX4uIF0%2FYJtC6jwaj5O2BfBYcfVNCzwfEs4esYaXyqbtwZvX3P3cXgITHVsqUdCDPAOGELLEcUtVtquM4hofSh%2F5lk9IHkgJUPD4StiHLHeE8hdb%2BEblk4%2BxtUuxzT124mxvROPf0v4bJhHmEL8QIoRUH52mwwdsxY%2F9FOznJ0JR1D%2FsBaDkix04H1MXNnvoMg7N390rIARmoYJZUQOjvC3%2FBn7O7caRUlyyWYkzpjuQUM40iAUo6ryFFYSul2adi7iDLuIdu5CgzlrgTcNNSW3tWrwMHdqClRbH9q0SBJHYKjCBx7wYaZ%2BrkEyuoMeb3lRQEujnw%2FtI6AdI%2BxWVpF%2Bz1f8nYlPZcgavw48xKrVmSMon5D5gdsezmHZrMXeS4F2hYZqpcMcEyeUesMG7Nzvgt1FX3Cwzs4ep%2B6876NW488fQ1SygCk2UhW0rzfjO--dG%2BnEhtWw%2FpfgYhv--mBjdhc7Fp6s2%2Byni6eICIQ%3D%3D'
        cookies = {i.split('=')[0]: i.split('=')[-1] for i in temp.split('; ')}

        yield scrapy.Request(url=url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        # pass
        # 登录github第一种方法：直接携带cookie登录
        # 验证是否登录成功（登录成功title标签text()为用户名）
        title = response.xpath('/html/head/title/text()').extract_first()
        print(title)


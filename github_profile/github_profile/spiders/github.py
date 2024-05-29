import scrapy
from scrapy_splash import SplashRequest, SplashFormRequest, SplashResponse
from github_profile.items import GithubProfileItem


class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]
    data = {
        'username': ..., # NOTE: your username or email address
        'password': ... # NOTE: your password
    }
    
    def start_requests(self):
        yield SplashRequest(url=r'https://github.com/login', callback=self.parse)
    
    def parse(self, response: SplashResponse):
        yield SplashFormRequest.from_response(response, url=r'https://github.com/session', formdata=self.data, callback=self.after_login)
        
    def after_login(self, response: SplashResponse):
        yield response.follow(url=r'https://github.com/%s' % self.data.get('username'), callback=self.profile)
        
    def profile(self, response: SplashResponse):
        item = GithubProfileItem()
        item['username'] = response.css('span.p-nickname::text').get()
        item['name'] = response.css('span.overflow-hidden::text').get()
        item['bio'] = response.css('div.user-profile-bio div::text').get()
        item['social_accounts'] = response.css('a.Link--primary::text').get()
        item['number_of_repositories'] = response.css('span.Counter::text').get()
        item['number_of_stars'] = response.css('span.Counter::text').getall()[-1]
        yield item
        

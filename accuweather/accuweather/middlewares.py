from scrapy.http import Request, Response
from fake_useragent import FakeUserAgent


class AccuweatherDownloaderMiddleware:
    user_agent = FakeUserAgent()
    
    def process_request(self, request: Request, spider):
        request.headers['User-Agent'] = self.user_agent.random
    
    def process_response(self, request: Request, response: Response, spider):
        return response

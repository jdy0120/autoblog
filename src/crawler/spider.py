import scrapy

class MySpider(scrapy.Spider):
  name = 'myspider'
  
  start_urls = [
    'https://map.naver.com/v5/search/%EC%82%BC%EC%B2%99%EC%8B%9C%20%EB%85%B8%EA%B3%A1%EB%A9%B4%20%EB%A7%9B%EC%A7%91/place/15034988?c=12,0,0,0,dh&placePath=%3Fentry%253Dpll'
  ]

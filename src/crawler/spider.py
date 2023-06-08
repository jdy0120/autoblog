import scrapy

class MySpider(scrapy.Spider):
  name = 'myspider'
  
  start_urls = [
    'http://example.com/'
  ]
  
  def parse(self, response):
    self.log('Visited %s' % response.url)

    # CSS 또는 XPath를 이용해 웹 페이지의 특정 부분을 선택합니다.
    # 이 예제에서는 <title> 태그의 텍스트를 선택합니다.
    title = response.css('title::text').get()

    yield {
        'title': title,
    }
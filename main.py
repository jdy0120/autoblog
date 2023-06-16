from src.crawler import MySpider
from src.crawler.spider import search_naver

if __name__ == "__main__":
    # Spider 인스턴스 생성
    spider = MySpider()
    
    
    # 크롤링 시작
    data = spider.parse('https://map.naver.com/v5/search/%EC%82%BC%EC%B2%99%EC%8B%9C%20%EB%85%B8%EA%B3%A1%EB%A9%B4%20%EB%A7%9B%EC%A7%91/place/15034988?c=12,0,0,0,dh&placePath=%3Fentry%253Dpll')
    
    search_naver('doyeon')

    # BlogApiHandler 인스턴스 생성
    # blog_api_handler = BlogApiHandler()

    # 크롤링한 데이터로 블로그 포스트 생성
    # for post in data:
    #     blog_api_handler.post_to_blog(post)
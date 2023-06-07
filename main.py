from src.crawler import Spider
from src.blog_poster import BlogApiHandler

if __name__ == "__main__":
    # Spider 인스턴스 생성
    spider = Spider()
    
    # 크롤링 시작
    data = spider.crawl()

    # BlogApiHandler 인스턴스 생성
    blog_api_handler = BlogApiHandler()

    # 크롤링한 데이터로 블로그 포스트 생성
    for post in data:
        blog_api_handler.post_to_blog(post)
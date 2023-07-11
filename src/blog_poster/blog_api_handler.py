import xmlrpc.client

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

wordpress_url = os.getenv("WORDPRESS_URL")
admin_id = os.getenv("ADMIN_ID")
admin_password = os.getenv("ADMIN_PASSWORD")

def CreatePost(title, content):
    content = {
        "post_title": title,
        "post_content": content,
        "post_status": "publish",  # 바로 게시하려면 'publish', 초안으로 저장하려면 'draft'
    }
    
    print(content)
    server = xmlrpc.client.ServerProxy(wordpress_url)
    
    post_id = server.wp.newPost(0, admin_id, admin_password, content)
    
    print(f"글이 작성되었습니다. ID: {post_id}")
    

import xmlrpc.client
import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

wordpress_url = os.getenv("WORDPRESS_URL")
admin_id = os.getenv("ADMIN_ID")
admin_password = os.getenv("ADMIN_PASSWORD")
google_maps_api_key = os.getenv("GOOGLE_MAP_API_KEY")

categories=["korean_restaurant"]
tags=["review", "information", "introduction", "korean restaurant" ]

def CreatePost(address,title, content):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_maps_api_key}"
    
    response = requests.get(url)
    
    resp_json_payload = response.json()
    googlemap = "\n\nGoogle Maps Location:\n"
    
    latitude = resp_json_payload['results'][0]['geometry']['location']['lat']
    longitude = resp_json_payload['results'][0]['geometry']['location']['lng']
    
    googlemap += f'''
    <iframe
        width="600"
        height="450"
        style="border:0"
        loading="lazy"
        allowfullscreen
        src="https://www.google.com/maps/embed/v1/view?key={google_maps_api_key}&center={latitude},{longitude}&zoom=18">
    </iframe>
    '''
    
    content = {
        "post_title": title,
        "post_content": '<h1>{0}</h1> \n {1}'.format(title,content) + googlemap,
        "post_status": "publish",  # 바로 게시하려면 'publish', 초안으로 저장하려면 'draft'
        "categories": categories,  # 카테고리는 ID로 지정해야 합니다.
        "mt_keyowrds": tags,
    }
    
    print(content)
    server = xmlrpc.client.ServerProxy(wordpress_url)
    
    post_id = server.wp.newPost(0, admin_id, admin_password, content)
    
    print(f"글이 작성되었습니다. ID: {post_id}")
    

import requests
from scrapy import Selector
import re


def get_likes(item, xpath_expression: str):
    likes = item.xpath(xpath_expression).get()
    likes = re.sub("\D", "", likes)
    return likes


def get_data(link_post: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }
    r = requests.get(
        url=link_post,
        headers=headers
    )
    page = Selector(text=r.text)
    post_id = page.xpath('//link[@rel="canonical"]/@href').get()
    post_id = re.search(r'\d+_\d+', post_id).group()
    likes = get_likes(page, './/div[@class="like_wrap"]/a/@aria-label')
    share = page.xpath('//b[@class="v_share"]/text()').get()
    views = page.xpath(
        '//span[@class="Socials__button_views "]/@aria-label').get()
    views = re.sub("\D", "", views)
    data = {
        'post_id': post_id,
        'url': r.url,
        'likes': likes,
        'share': share,
        'views': views
    }
    return data

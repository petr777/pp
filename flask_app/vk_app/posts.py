import json
from scrapy import Selector
import requests
import re


headers = {
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua-mobile": "?0",
    "x-requested-with": "XMLHttpRequest",
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
}


def get_post_id(item, xpath_expression: str):
    post_id = item.xpath(xpath_expression).get()
    post_id = re.search(r'\d+_\d+', post_id).group()
    return post_id


def get_likes(item, xpath_expression: str):
    likes = item.xpath(xpath_expression).get()
    likes = re.sub("\D", "", likes)
    return likes


def get_views(item, xpath_expression: str):
    views = item.xpath(xpath_expression).get()
    views = re.sub("\D", "", views)
    return views


def get_share(item, xpath_expression: str):
    share = item.xpath(xpath_expression).get()
    if share:
        share = re.sub("\D", "", share)
        return share


def get_data(alias: str, skip: int = 0):
    url = f"https://m.vk.com/{alias}?offset={skip}"
    data = {
        '_ajax': 1
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    JSON = r.json()
    html = JSON['html']
    page = Selector(text=html)

    data = []
    for item in page.xpath('.//div[@class="wall_item"]'):
        post_id = get_post_id(item, './/a[@class="wi_date"]/@href')
        data.append({
            'post_id': post_id,
            'url': 'https://m.vk.com/wall' + post_id,
            'likes': get_likes(
                item, './/div[@class="like_wrap"]/a/@aria-label'),
            'share': get_share(
                item, './/b[@class="v_share"]/text()'),
            'views': get_views(
                item, './/span[@class="Socials__button_views "]/@aria-label')
        })
    return data

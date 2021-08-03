import requests
import html_text
from scrapy import Selector
import re


def get_params_acaunt(page, xpath_expression: str) -> int:
    elem = page.xpath(xpath_expression).get()
    elem = html_text.extract_text(elem)
    elem = re.sub("\D", "", elem)
    return int(elem)


def get_avatar_url(page, xpath_expression: str):
    elem = page.xpath(xpath_expression).get()
    elem = re.findall(r"url\('(.*?)'\)", elem)[0]
    elem = elem.replace(';', '&')
    return elem


def get_profile_id(page, xpath_expression: str) -> int:
    elem = page.xpath(xpath_expression).get()
    elem = re.sub("\D", "", elem)
    return int(elem)


def get_data(alias: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36'
    }
    r = requests.get(
        f'https://m.vk.com/{alias}?act=info',
        headers=headers
    )
    if r.status_code == 200:
        page = Selector(text=r.text)
        data = {
            'profile_id': get_profile_id(
                page, '//a[contains(@href,"/groups")]/@href'),
            'avatar_url': get_avatar_url(
                page, '//a[contains(@href,"from=profile")]'),
            'following': get_params_acaunt(
                page, '//a[contains(@href,"?act=idols")]'),
            'followers': get_params_acaunt(
                page, '//a[contains(@href,"?act=fans")]')
        }
        return data
    return None

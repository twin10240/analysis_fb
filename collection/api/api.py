from .json_request import json_request
from urllib.parse import urlencode

ACCESS_TOKEN = '%s|%s' % ('1401896856595921', '99879a831892832bf8c99e823bcb594c')
BASE_URL_FB_API = 'https://graph.facebook.com/v2.10'
LIMIT_REQUEST = 50


def fb_gen_url(base=BASE_URL_FB_API, node='', **params):
    # urlencode -> params를 url 파라미터로 바꿔주는 메서드
    return '%s/%s/?%s' % (base, node, urlencode(params))


def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)

    json_result = json_request(url=url)
    return json_result.get('id')


def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(node=fb_name_to_id(pagename)+"/posts",
                     fields='id,message,link,name,type,shares,created_time,reactions,comments.limit(0).summary(true)',
                     since=since, until=until, limit=LIMIT_REQUEST, access_token=ACCESS_TOKEN)

    while True:
        json_result = json_request(url=url)
        paging = json_result.get('paging')

        posts = json_result.get('data')

        yield posts

        url = paging.get('next')
        if url is None:
            break


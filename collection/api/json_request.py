import sys
from datetime import datetime
from urllib.request import Request, urlopen
import json


def json_request(url='', encording='utf-8', success=None,
                 error=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)

        resp_body = resp.read().decode(encording)
        json_result = json.loads(resp_body)

        print('%s : success for request [%s]' % (datetime.now(), url))

        # callable -> 부를 수 있는지 확인하는 메서드
        if callable(success) is False:
            return json_result

        success(json_result)
    except Exception as e:
        callable(error) and error(e)

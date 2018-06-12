# http test
import sys
from urllib.request import Request, urlopen
from datetime import *
import json

#def print_error():
#    print("%s:%s" % (e, datetime.now()), file=sys.stderr)

#html_request(url='http://www.naver.com')
#html_request(url='http://www.naver.com',success=print_html)
#html_request(url='http://www.naver.com',success=print_html,error=)
#처리결과에 따라 실행 메소드 지정.성공하면 print_html함수를 실행하라
def html_request(url='',
                 encoding='utf-8',
                 success=None,  #success를 안넣어도 none으로 세팅
                 error=lambda e:print("%s:%s" % (e, datetime.now()), file=sys.stderr)#람다 이름없는 함수 적용 #error=print_error     #에러처리방식도 함수화
                 ):
    try:
        request = Request(url)
        resp = urlopen(request)
        html = resp.read().decode(encoding)# 바이트를 문자열로 디코딩(3byte씪 쪼개서 문자로만듬)

        print('%s : success for request [%s]'%(datetime.now(),url))

        if callable(success) is False: # callable 호출할수 있는 함수가 아니면
            return html

        success(html)

    except Exception as e:
        if callable(error) is True: #error 함수가 호출할수 있는 함수이면
            error(e)

def json_request(url='',
                 encoding='utf-8',
                 success=None,
                 error = lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        resp=urlopen(Request(url))
        resp_body=resp.read().decode(encoding)# 바이트를 문자열로 디코딩(3byte씪 쪼개서 문자로만듬)
        json_result = json.loads(resp_body)  # json lib를 이용하여 json에서 다루는 객체형태로 응답을 변경

        print('%s : success for request [%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result
        success(json_result)

    except Exception as e:
        callable(error) and error(e)



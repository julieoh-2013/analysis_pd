from _datetime import datetime
import math
from urllib.parse import urlencode
from .web_request import json_request


'''
url = pdapi.pd_gen_url(
    'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    YM='{0:04d}{1:02d}'.format(2017, 1),
    SIDO='서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    pageNo=1)
'''
BASE_URL_FB_API='http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'
SERVICE_KEY='O4GTUjJhqd2Zh%2FUKol%2FD%2F03SF57S%2B1Kr%2FEF55PYYb3zh0ZeimbMRClwaUBScosK6KGB7rJHgnlr4QCF%2FIpTV1Q%3D%3D'


def pd_gen_url(endpoint,**param):
    url = '%s?%s&serviceKey=%s' % (endpoint,urlencode(param),SERVICE_KEY)
    return url


def pd_fetch_foreign_visitor(country_code, year, month):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url = pd_gen_url(endpoint,
                     YM='{0:04d}{1:02d}'.format(year,month), #201701
                     NAT_CD=country_code,
                     ED_CD='E',  # D: 국민 해외 관광객,  E: 방한 해외 관광객
                     _type='json'
                     )
    json_result = json_request(url)

    json_response = json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')
    if 'OK'!=result_message:
        print('%s Error[%s] for request %s', (datetime.now(),result_message,url))
        return None
    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item')if isinstance(json_items, dict) else None  # items가 dict 형 이면


#for items in api.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
def  pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):

    isnext = True
    pgno=1

    ym = str(year) +'0'+str(month) if month<10 else str(year)+str(month)
    while isnext is True:
        url = pd_gen_url(BASE_URL_FB_API,
                         YM=ym,
                         SIDO=district1,
                         GUNGU=district2,
                         RES_NM=tourspot,
                         _type='json',
                         pageno=pgno,
                         numOfRows=100)

        json_result = json_request(url=url)
        resp = None if json_result is None else json_result['response']
        body = None if resp is None else resp['body']
        items =None if body is None else body['items']

        if isinstance(items, dict):
            item = items.get('item')
        else :
            isnext = False
            item = None

        nrow = body.get('numOfRows')
        totcnt = body.get('totalCount')

        if totcnt == 0:
            break

        last_page = math.ceil(totcnt/nrow) # math.ceil(tn/n) 나눈몫정수중 높은 정수 줌 2.4 는 3줌 작은수주는건 floor
        if pgno == last_page:
            isnext = False
        else:
            pgno = pgno + 1

    yield item
'''
        if pgno < get_tot_pgno(totcnt, nrow):
            pgno = pgno + 1
        else :
            isnext = False

    yield item

def get_tot_pgno(tot, rnum):
    if tot % rnum == 0:
        return tot // rnum
    else:
        return tot // rnum + 1
'''

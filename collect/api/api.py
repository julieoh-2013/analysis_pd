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
ACCESS_TOKEN='O4GTUjJhqd2Zh%2FUKol%2FD%2F03SF57S%2B1Kr%2FEF55PYYb3zh0ZeimbMRClwaUBScosK6KGB7rJHgnlr4QCF%2FIpTV1Q%3D%3D'
def pd_gen_url(base,**params):
    url = '%s?%s&serviceKey=%s' % (base,urlencode(params),ACCESS_TOKEN)
    return url

#for items in api.pd_fetch_tourspot_visitor(district1='서울특별시', year=2012, month=7):
def  pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):
    url = pd_gen_url(BASE_URL_FB_API,
                     YM='{0:04d}{1:02d}'.format(year, month),
                     SIDO=district1,
                     GUNGU=district2,
                     RES_NM=tourspot,
                    _type = 'json',
                     pageNo = 1,
                     numOfRows=100)


    isnext = True
    while isnext is True:
        json_result = json_request(url=url)
        items = None if json_result is None else json_result['response']['body']['items'].get('item')
        print('items : ',items)
    yield items

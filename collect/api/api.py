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

        items = None if json_result is None else json_result['response']['body']['items'].get('item')
        nrow = None if json_result is None else json_result['response']['body'].get('numOfRows')
        totcnt = None if json_result is None else json_result['response']['body'].get('totalCount')

        if pgno < get_tot_pgno(totcnt, nrow):
            pgno = pgno + 1
        else :
            isnext = False

    yield items

def get_tot_pgno(tot, rnum):
    if tot % rnum == 0:
        return tot // rnum
    else:
        return tot // rnum + 1
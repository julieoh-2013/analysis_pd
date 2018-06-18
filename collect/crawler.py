from datetime import datetime, timedelta

import os

from .api import api
import json

RESULT_DIRECTORY = '__results__/crawling'
'''
 count_locals :23455      'csNatCnt':48983  내국인방문객수
 count_forigner:245325    'csForCnt':50216, 외국인방문객수 
 tourist_spot:창덕궁       'resNm':'창덕궁',  관광지
 date:201701             'ym':201207        년월
 restrict1:서울특별시      'sido':'서울특별시', 시도
 restrict2;종로구		  'gungu':'종로구',	  시군구
 ===========================
--'addrCd':1111,
'csForCnt':50216,
'csNatCnt':48983,
'gungu':'종로구',
'resNm':'창덕궁',
--'rnum':1,
'sido':'서울특별시',
'ym':201207
'''
def preprocess_item(item):

    del item['addrCd']
    del item['rnum']

    # 내국인방문객수
    if 'csNatCnt' not in item:
        item['csNatCnt'] = 0
    else:
        item['count_locals'] = item['csNatCnt']
        del item['csNatCnt']

    # 외국인방문객수
    if 'csForCnt' not in item:
        item['csForCnt'] = 0
    else:
        item['count_forigner'] = item['csForCnt']
        del item['csForCnt']

    # 관광지
    if 'resNm' not in item:
        item['tourist_spot'] = ''
    else:
        item['tourist_spot'] = item['resNm']
        del item['resNm']

    # 년월
    if 'ym' not in item:
        item['date'] = 0
    else:
        item['date'] = item['ym']
        del item['ym']

    # 시도
    if 'sido' not in item:
        item['restrict1'] = ''
    else:
        item['restrict1'] = item['sido']
        del item['sido']

    # 시도
    if 'gungu' not in item:
        item['restrict2'] = ''
    else:
        item['restrict2'] = item['gungu']
        del item['gungu']
'''
    {
        "country_code": 275,
        "country_name": "미국",
        "date": 201701,
        "visit_count": 55739
    },
    {
      --  'ed':'방한외래관광객',
      --  'edCd':'E',
        'natCd':275,
        'natKorNm':'미 국',
        'num':57212,
      --  'rnum':1,
        'ym':201701
    }
'''
def preprocess_foreign_visitor(data):
    #ed
    del data['ed']

    #edCd
    del data['edCd']

    #rnum
    del data['rnum']

    #나라코드
    data['country_code'] = data['natCd']
    del data['natCd']

    #나라이름
    data['country_name'] = data['natKorNm'].replace(' ','')
    del data['natKorNm']

    #방문자수
    data['visit_count'] = data['num']
    del data['num']

    #년월
    if 'ym' not in data:
        data['date'] =''
    else:
        data['date'] = data['ym']
        del data['ym']


def crawling_foreign_visitor(country, start_year, end_year):
    results = []

    for year in range(start_year, end_year+1):
        for month in range(1,13):
            data = api.pd_fetch_foreign_visitor(country[1],year,month)
            if data is None:
                continue    #중국 코드 잘못넣어서 결과 없어도 다음 나라거 가져오게

            preprocess_foreign_visitor(data)
            results.append(data)  # append 리스트 끝에  data 객체추가
            #results += data # += 리스트  끝에 data 값 추가

    #save data to file  : 나라_코드_foreign_visitor_2017_2017.json
    filename = '%s/%s(%s)_foreignvisitor_%s_%s.json'%(RESULT_DIRECTORY,country[0],country[1],start_year,end_year)

    with open(filename,'w',encoding='utf-8') as outfile: # 파일 헨들러 이름 outfile
        json_strig = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False) #객체를 str로 변환해줌
        outfile.write(json_strig)


def crawlling_tourspot_visitor(district, start_year, end_year):
    results = []
    # 서울특별시_tourinstspot_2017_2017.json
    filename = '%s/%s_%s_%s_%s.json' % (RESULT_DIRECTORY, district,'tourinstspot', start_year, end_year)

    curyear=datetime.today().year
    untilmonth = datetime.today().month+1 if(str(curyear) == start_year) else 13

    for year in range(int(start_year), int(end_year)+1):
        for month in range(1,untilmonth):
            for items in api.pd_fetch_tourspot_visitor(district1=district,year=year,month=month):
                for item in items:
                    preprocess_item(item)
                results += items

    # save results to file
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)
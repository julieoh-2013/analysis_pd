import collect
from config import CONFIG
 # collect.crawlling_tourspot_visitor(district='서울특별시', start_year=2017, end_year=2017)
if __name__ == '__main__':

   #collect

    collect.crawlling_tourspot_visitor(
                                        district=CONFIG['district'],
                                         **CONFIG['common'] )


    for country in CONFIG['contries']:
       collect.crawling_foreign_visitor( country,
                                        **CONFIG['common'] )
                                       # start_year=CONFIG['common']['start_year'],
                                       # end_year= CONFIG['common']['end_year'])
                                       # 튜플은 다른타입데이터 들어감 리스트는 같은타입 데이터가 들어감







   #analysis


   #visualize


"""

items = [
  #  {'district': '서울특별시', 'start_year': '2017', 'end_year': '2017'},
   # {'district': '부산광역시', 'start_year': '2016', 'end_year': '2016'},
    {'district': '인천광역시', 'start_year': '2018', 'end_year': '2018'}
]

# collection
for item in items:
    collect.crawlling_tourspot_visitor(**item)

"""
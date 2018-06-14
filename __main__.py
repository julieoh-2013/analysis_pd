import collect

 # collect.crawlling_tourspot_visitor(district='서울특별시', start_year=2017, end_year=2017)
if __name__ == '__main__':

   #collect

   for country in [('중국', 112), ('일본', 130), ('미국', 275)]:
       collect.crawling_foreign_visitor(country, 2017, 2017) # 튜플은 다른타입데이터 들어감 리스트는 같은타입 데이터가 들어감

   '''
   collect.crawlling_tourspot_visitor(
                                        district='서울특별시', 
                                        start_year=2017, 
                                        end_year=2017)
    '''




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
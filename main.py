import collect
"""
 # collect.crawlling_tourspot_visitor(district='서울특별시', start_year=2017, end_year=2017)
if __name__ == '__main__':
    collect.crawlling_tourspot_visitor(district='서울특별시', start_year=2017, end_year=2017)
"""

items = [
    {'district': '서울특별시', 'start_year': '2017', 'end_year': '2017'},
    {'district': '부산광역시', 'start_year': '2016', 'end_year': '2016'}
]

# collection
for item in items:
    collect.crawlling_tourspot_visitor(**item)

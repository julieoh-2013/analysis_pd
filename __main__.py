import collect
import analyze
import visualize
from config import CONFIG
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    resultfiles = dict()

    #collect
    resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(
                                                    district=CONFIG['district'],
                                                    **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['contries']:
        rf = collect.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    #1. analysis and visualize
    #result_analsis = analyze.analysis_correlation(resultfiles)
    #visualize.graph_scatter(result_analsis)
    #print(result_analsis)

    #2. analysis and visualize (for문-dataframe만들고)
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    graph_table = pd.DataFrame(result_analysis,columns=['tourspot','r_중국','r_일본','r_미국'])
    graph_table = graph_table.set_index('tourspot')

    graph_table.plot(kind='bar', rot=70)
    plt.show()


    #장소별로 방문자수와 일본인 입국자수와 상관계수 구하기 장소별 상관계수3개나옴
    # dataframe = 안에서 머지
    # tourspot r_중국  r_일본  r_미국 중국입국자수 일본입국자수 미국입국자수 중국방문자수....
    #  경복궁     0.2  0.33    0.88
    #  경복궁     0.2  0.33    0.88  (딕셔너리 리스트에 넣어서)
    '''
    graph_table = pd.DataFrame(result_analysis, colums=['tourspot','r_중국','r_일본','r_미국',])
    graph_table= graph_table.set_index('tourspot')
    graph_table.plot(kind='bar')
    plt.show()
    '''
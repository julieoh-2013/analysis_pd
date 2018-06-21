import json
import pandas as pd
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
import math

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())
    #print(temp_tourspotvisitor_table)
    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())
        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        foreignvisitor_table = foreignvisitor_table.set_index('date')
        #인덱스로 머징 (기본은 공통칼럼으로)
        merge_table = pd.merge(temp_tourspotvisitor_table,
                 foreignvisitor_table,
                 left_index=True,
                 right_index=True
                 )
        # date count_foreigner country_name  visit_count
        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])
        print(foreignvisitor_table['country_name'].unique())
        country_name = foreignvisitor_table['country_name'].unique().item(0)#<class 'numpy.ndarray'>.item() #ndarray.item(*args)

        #상관계수추출 scipy설치
        r = correlation_coefficient(x,y)
        #r = ss.pearsonr(x,y)[0]  #피어슨 상관계수
        #r = np.corrcoef(x,y)[0]

        #data = {'x':x, 'y':y,'country_name':country_name, 'r':r}
        results.append({'x':x, 'y':y,'country_name':country_name, 'r':r})

        merge_table['visit_count'].plot(kind='bar')
        plt.show()
    return results


def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'],'r',encoding='utf-8') as infile :
        json_data = json.loads(infile.read())
    tourspotvisitor_table = pd.DataFrame(json_data, columns=['tourist_spot','date','count_foreigner'])
    tourist_spots = tourspotvisitor_table['tourist_spot'].unique()

    results = []
    for spot in tourist_spots:
        data = {'tourspot': spot}
        s = tourspotvisitor_table['tourist_spot'] == spot
        temp_table = tourspotvisitor_table[s]
        temp_table = temp_table.set_index('date')

        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())
            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            foreignvisitor_table = foreignvisitor_table.set_index('date')

            # 인덱스로 머징 (기본은 공통칼럼으로)
            merge_table = pd.merge(temp_table,
                                   foreignvisitor_table,
                                   left_index=True,
                                   right_index=True
                                   )
            country_name = foreignvisitor_table['country_name'].unique().item(0)
            # 상관계수추출 scipy설치
            x = list(merge_table['count_foreigner'])
            y = list(merge_table['visit_count'])
            r = correlation_coefficient(x, y)

            data['r_' + country_name] = r

        results.append(data)

    graph_table = pd.DataFrame(results, columns=['tourspot', 'r_중국', 'r_일본', 'r_미국', ])
    graph_table = graph_table.set_index('tourspot')
    graph_table.plot(kind='bar', rot = 70)
    plt.show()

'''
    [{'tourspot': '창덕궁', 'r_중국': -0.05787996838309703, 'r_일본': 0.18113398877560832, 'r_미국': 0.15157690000865773}, 
    {'tourspot': '경복궁', 'r_중국': -0.8435333683208608, 'r_일본': -0.6908586912392769, 'r_미국': -0.8041107208313881}, 
    {'tourspot': '창경궁', 'r_중국': 0.3302835585547996, 'r_일본': 0.1897358329486392, 'r_미국': 0.4564453800391374}, 


#json 로딩, 머지, 상관계수

#장소별로 방문자수와 일본인 입국자수와 상관계수 구하기 장소별 상관계수3개나옴
#dataframe = 안에서 머지
# tourspot r_중국  r_일본  r_미국 중국입국자수 일본입국자수 미국입국자수 중국방문자수....
#  경복궁     0.2  0.33    0.88
#  경복궁     0.33  0.32    0.22  (딕셔너리 리스트에 넣어서)

graph_table = pd.DataFrame(result_analysis, colums=['tourspot','r_중국','r_일본','r_미국',])
graph_table= graph_table.set_index('tourspot')
graph_table.plot(kind='bar')
plt.show()
'''

def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError:
        r = 0.0

    return r



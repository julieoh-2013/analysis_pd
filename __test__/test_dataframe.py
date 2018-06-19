import pandas as pd

#가가 시리즈 두개 만들고, 각 시리즈에 이름 부여, 두개를 합힘 = 데이터 프레임 생성
#Series와 dict를 활용해 만든 dataframe
d = {
   'one' : pd.Series([1,2,3], index=['a','b','c']),
   'two': pd.Series([10,20,30,40], index=['a','b','c','d'])
}
df = pd.DataFrame(d)
print(df)


#List와 dict를 사용해 만든 dataframe
# 제약 조건 : 세 시리즈의 키값이 같아야 한다.
data =[
    {'name':'둘리','age':10, 'phone':'010-111-1111'},
    {'name':'마이콜','age':30, 'phone':'010-222-2222'},
    {'name':'도넛','age':30, 'phone':'010-333-3333'}
]
df = pd.DataFrame(data)
print(df)

df2 = pd.DataFrame(df, columns=('name','phone'))
print(df2)

# 데이터 추가 (열추가)
df2['height'] = [150, 160, 170]
print(df2)

# 인덱스 선택
df3 = df2.set_index('name')
print(df3)

# 컬럼 선택 (시리즈하나 선택해 받아옴)
s = df2['name']
print(s, type(s))

#merge
#공통된 열이 있어야 머지 가능, 없으면 인덱스로 하라고 지정해야함
df4 = pd.DataFrame([{'sido': '서울'}, {'sido': '부산'}, {'sido': '전주'}])
df5 = pd.merge(df2, df4, left_index=True, right_index=True)

print(df5)


# merge and join
# 공통 열의 고객번호를 기준으로 데이터를 합친다
# 이때 기본적으로 양쪽에 데이터 프레임에 모두 수가 존재하는 데이터만 합쳐친다.
# inner join방식 : 양쪽에 둘다 매칭되는 경우만 합침
df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']})

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]})
df3= pd.merge(df1, df2)
print(df3)

# outter join방식은 키값이 한쪽에만 있어도 양쪽데이터를 모두 가져온다
# full outter join
df3 = pd.merge(df1, df2, how='outer')
print(df3)

# left outter join 첫번째 칼럼(파라미터)의 데이터 프레임의 데이터를 전부 가져오는 방식
# right outter join 두번째 칼럼(파라미터) 의 데이터 프레임의 데이터를 전부 가져오는 방식
df3 = pd.merge(df1, df2, how='left')
print(df3)

df3 = pd.merge(df1, df2, how='right')
print(df3)

# 조인 기준 열은 on 인수로 명시적 설정이 가능
df1 = pd.DataFrame({'성별': ['남자', '남자', '여자'],
                    '연령': ['미성년자', '성인', '미성년자'],
                    '매출1': [1, 2, 3]})

df2 = pd.DataFrame({'성별': ['남자', '남자', '여자', '여자'],
                    '연령': ['미성년자', '미성년자', '미성년자', '성인'],
                    '매출2': [4, 5, 6, 7]})

df3 = pd.merge(df1, df2)
print(df3)

df3 = pd.merge(df1, df2, on=['성별', '연령'])
print(df3)

df3 = pd.merge(df1, df2, on=['성별'])
print(df3)








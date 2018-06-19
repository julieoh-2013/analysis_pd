import pandas as pd

price = [92600, 92400, 92100, 94300, 92300]

s = pd.Series(price)
print(s)
print(s[0], s[1])

# index를 부여할때는 반드시 데이터 개수와 같아야 한다.
s = pd.Series(
[92600, 92400, 92100, 94300, 92300],
    index=['2017-01-01', '2017-02-02', '2017-03-03', '2017-04-04', '2017-05-05']
)
print(s)
print(s[1],s['2017-02-02'])
# 스칼라 값으로 초기화할때는 index값이 반드시 필요 하다
s1 = pd.Series(7,index=['a','b','c','d'])
print(s1)

#딕션너리로 초기활 할때는 인덱스 키가 바로 셋팅된다
d = {'a':10, 'b':20, 'c':30, 'd':40}
s1=pd.Series(d)
print(s1)

s1 = pd.Series(d, index=['A','B','C'])
print(s1)

s1 = pd.Series(d, index=['a','b','c','d'])
print(s1)


#순회 (index와 values라는 속성으로 시리즈 접근 가능하다.
for date in s.index:
    print(' date: ' ,date,end=' ')
else:
    print()


for price in s.values:
    print(' price: ', price, end=' ')
else:
    print()

#연산
s1=pd.Series([10,20,30], index=['A','B','C'])
s2=pd.Series([10,20,30], index=['B','C','D'])

s3=s1+s2
print(s3,type(s3))

s3=s1-s2
print(s3,type(s3))

s3=s1*s2
print(s3,type(s3))

s3=s1/s2
print(s3,type(s3))

s3=s1*3
print(s3,type(s3))
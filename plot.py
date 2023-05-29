import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Read the data from the csv file
data = pd.read_csv('C:\\Users\hoseong\OneDrive\Coding\DA_forum\전자상거래_및_통신판매_이용시_구매_방식_20230529230805.csv')

# 한글 글꼴 설정
plt.rc('font', family='NanumGothic')
plt.rc('axes', unicode_minus=False)

print(data)

# 전체
all = data.iloc[0:1, 0:25]

# 사례수 삭제
all = all.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)

print(all)

# 성별
sex = data.iloc[1:3, 0:25]

# 사례수 삭제
sex = sex.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(sex)

# 연령
age = data.iloc[3:10, 0:25]

# 사례수 삭제
age = age.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(age)

# 월평균소득
income = data.iloc[10:18, 0:25]

# 사례수 삭제
income = income.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(income)

# 학력
education = data.iloc[18:23, 0:25]

# 사례수 삭제
education = education.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(education)

# 지역
location = data.iloc[23:40, 0:25]

# 사례수 삭제
location = location.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(location)

# 종사상지위
job = data.iloc[42:47, 0:25]

# 사례수 삭제
job = job.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)

print(job)

# 상세직업
job_detail = data.iloc[47:61, 0:25]

# 사례수 삭제
job_detail = job_detail.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)

print(job_detail)

# 주택형태
house = data.iloc[61:66, 0:25]

# 사례수 삭제
house = house.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)

print(house)

# 가족구성
family = data.iloc[66:71, 0:25]

# 사례수 삭제
family = family.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7'],
        axis=1)

print(family)

# 가구원수
family_num = data.iloc[71:74, 0:25]

# 사례수 삭제
family_num = family_num.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7'],
        axis=1)

print(family_num)

# 가구주와의관계
relation = data.iloc[74:83, 0:25]

# 사례수 삭제
relation = relation.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7'],
        axis=1)

print(relation)


def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))  # round: 반올림, sum: array 다 더하기
    return "{:.1f}%\n원값: {:d}%".format(pct, absolute)


# all, sex, age, income, education, job, job_detail, house, family, family_num, relation
data_and_titles = [
        (all.values[0][0:8].astype(float), "2021 전체_소계"), (all.values[0][9:16].astype(float), "2022 전체_소계"),

        (sex.values[0][0:8].astype(float), "2021 성별_남"), (sex.values[0][9:16].astype(float), "2022 성별_남"),
        (sex.values[1][0:8].astype(float), "2021 성별_여"), (sex.values[1][9:16].astype(float), "2022 성별_여"),

        (age.values[0][0:8].astype(float), "2021 연령_만10-19세"), (age.values[0][9:16].astype(float), "2022 연령_만10-19세"),
        (age.values[1][0:8].astype(float), "2021 연령_만20-29세"), (age.values[1][9:16].astype(float), "2022 연령_만20-29세"),
        (age.values[2][0:8].astype(float), "2021 연령_만30-39세"), (age.values[2][9:16].astype(float), "2022 연령_만30-39세"),
        (age.values[3][0:8].astype(float), "2021 연령_만40-49세"), (age.values[3][9:16].astype(float), "2022 연령_만40-49세"),
        (age.values[4][0:8].astype(float), "2021 연령_만50-59세"), (age.values[4][9:16].astype(float), "2022 연령_만50-59세"),
        (age.values[5][0:8].astype(float), "2021 연령_만60-69세"), (age.values[5][9:16].astype(float), "2022 연령_만60-69세"),
        (age.values[6][0:8].astype(float), "2021 연령_만70세이상"), (age.values[6][9:16].astype(float), "2022 연령_만70세이상"),

        (income.values[0][0:8].astype(float), "2021 월평균소득_소득없음"),
        (income.values[0][9:16].astype(float), "2021 월평균소득_소득없음"),
        (income.values[1][0:8].astype(float), "2021 월평균소득_50만원미만"),
        (income.values[1][9:16].astype(float), "2022 월평균소득_50만원미만"),
        (income.values[2][0:8].astype(float), "2021 월평균소득_50-100만원미만"),
        (income.values[2][9:16].astype(float), "2022 월평균소득_50-100만원미만"),
        (income.values[3][0:8].astype(float), "2021 월평균소득_100-200만원미만"),
        (income.values[3][9:16].astype(float), "2022 월평균소득_100-200만원미만"),
        (income.values[4][0:8].astype(float), "2021 월평균소득_200-300만원미만"),
        (income.values[4][9:16].astype(float), "2022 월평균소득_200-300만원미만"),
        (income.values[5][0:8].astype(float), "2021 월평균소득_300-400만원미만"),
        (income.values[5][9:16].astype(float), "2022 월평균소득_300-400만원미만"),
        (income.values[6][0:8].astype(float), "2021 월평균소득_500만원이상"),
        (income.values[6][9:16].astype(float), "2022 월평균소득_500만원이상"),

        (education.values[0][0:8].astype(float), "2021 학력_초졸이하"),
        (education.values[0][9:16].astype(float), "2022 학력_초졸이하"),
        (education.values[0][0:8].astype(float), "2021 학력_중졸이하"),
        (education.values[0][9:16].astype(float), "2022 학력_중졸이하"),
        (education.values[0][0:8].astype(float), "2021 학력_고졸이하"),
        (education.values[0][9:16].astype(float), "2022 학력_고졸이하"),
        (education.values[0][0:8].astype(float), "2021 학력_대졸이하"),
        (education.values[0][9:16].astype(float), "2022 학력_대졸이하"),
        (education.values[0][0:8].astype(float), "2021 학력_대학원재학이상"),
        (education.values[0][9:16].astype(float), "2022 학력_대학원재학이상"),

        (location.values[0][0:8].astype(float), "2021 지역_서울"), (location.values[0][9:16].astype(float), "2022 지역_서울"),
        (location.values[1][0:8].astype(float), "2021 지역_부산"), (location.values[1][9:16].astype(float), "2022 지역_부산"),
        (location.values[2][0:8].astype(float), "2021 지역_대구"), (location.values[2][9:16].astype(float), "2022 지역_대구"),
        (location.values[3][0:8].astype(float), "2021 지역_인천"), (location.values[3][9:16].astype(float), "2022 지역_인천"),
        (location.values[4][0:8].astype(float), "2021 지역_광주"), (location.values[4][9:16].astype(float), "2022 지역_광주"),
        (location.values[5][0:8].astype(float), "2021 지역_대전"), (location.values[5][9:16].astype(float), "2022 지역_대전"),
        (location.values[6][0:8].astype(float), "2021 지역_울산"), (location.values[6][9:16].astype(float), "2022 지역_울산"),
        (location.values[7][0:8].astype(float), "2021 지역_세종"), (location.values[7][9:16].astype(float), "2022 지역_세종"),
        (location.values[8][0:8].astype(float), "2021 지역_경기"), (location.values[8][9:16].astype(float), "2022 지역_경기"),
        (location.values[9][0:8].astype(float), "2021 지역_강원"), (location.values[9][9:16].astype(float), "2022 지역_강원"),
        (location.values[10][0:8].astype(float), "2021 지역_충북"), (location.values[10][9:16].astype(float), "2022 지역_충북"),
        (location.values[11][0:8].astype(float), "2021 지역_충남"), (location.values[11][9:16].astype(float), "2022 지역_충남"),
        (location.values[12][0:8].astype(float), "2021 지역_전북"), (location.values[12][9:16].astype(float), "2022 지역_전북"),
        (location.values[13][0:8].astype(float), "2021 지역_전남"), (location.values[13][9:16].astype(float), "2022 지역_전남"),
        (location.values[14][0:8].astype(float), "2021 지역_경북"), (location.values[14][9:16].astype(float), "2022 지역_경북"),
        (location.values[15][0:8].astype(float), "2021 지역_경남"), (location.values[15][9:16].astype(float), "2022 지역_경남"),
        (location.values[16][0:8].astype(float), "2021 지역_제주"), (location.values[16][9:16].astype(float), "2022 지역_제주"),

        (job.values[0][0:8].astype(float), "2021 종사상지위_임금근로자"), (job.values[0][9:16].astype(float), "2022 종사상지위_임금근로자"),
        (job.values[1][0:8].astype(float), "2021 종사상지위_고용주"), (job.values[1][9:16].astype(float), "2022 종사상지위_고용주"),
        (job.values[2][0:8].astype(float), "2021 종사상지위_단독자영업자"),
        (job.values[2][9:16].astype(float), "2022 종사상지위_단독자영업자"),
        (job.values[3][0:8].astype(float), "2021 종사상지위_무급가족종사자"),
        (job.values[3][9:16].astype(float), "2022 종사상지위_무급가족종사자"),
        (job.values[4][0:8].astype(float), "2021 종사상지위_무직"), (job.values[4][9:16].astype(float), "2022 종사상지위_무직"),

        (job_detail.values[0][0:8].astype(float), "2021 상세직업_관리자"),
        (job_detail.values[0][9:16].astype(float), "2022 상세직업_관리자"),
        (job_detail.values[1][0:8].astype(float), "2021 상세직업_전문가및관련종사자"),
        (job_detail.values[1][9:16].astype(float), "2022 상세직업_전문가및관련종사자"),
        (job_detail.values[2][0:8].astype(float), "2021 상세직업_사무종사자"),
        (job_detail.values[2][9:16].astype(float), "2022 상세직업_사무종사자"),
        (job_detail.values[3][0:8].astype(float), "2021 상세직업_서비스종사자"),
        (job_detail.values[3][9:16].astype(float), "2022 상세직업_서비스종사자"),
        (job_detail.values[4][0:8].astype(float), "2021 상세직업_판매종사자"),
        (job_detail.values[4][9:16].astype(float), "2022 상세직업_판매종사자"),
        (job_detail.values[5][0:8].astype(float), "2021 상세직업_농림어업종사자"),
        (job_detail.values[5][9:16].astype(float), "2022 상세직업_농림어업종사자"),
        (job_detail.values[6][0:8].astype(float), "2021 상세직업_기능원및관련기능종사자"),
        (job_detail.values[6][9:16].astype(float), "2022 상세직업_기능원및관련기능종사자"),
        (job_detail.values[7][0:8].astype(float), "2021 상세직업_장치기계조작및조립종사자"),
        (job_detail.values[7][9:16].astype(float), "2022 상세직업_장치기계조작및조립종사자"),
        (job_detail.values[8][0:8].astype(float), "2021 상세직업_단순노무종사자"),
        (job_detail.values[8][9:16].astype(float), "2022 상세직업_단순노무종사자"),
        (job_detail.values[9][0:8].astype(float), "2021 상세직업_직업군인"),
        (job_detail.values[9][9:16].astype(float), "2022 상세직업_직업군인"),
        (job_detail.values[10][0:8].astype(float), "2021 상세직업_학생"),
        (job_detail.values[10][9:16].astype(float), "2022 상세직업_학생"),
        (job_detail.values[11][0:8].astype(float), "2021 상세직업_전업주부"),
        (job_detail.values[11][9:16].astype(float), "2022 상세직업_전업주부"),
        (job_detail.values[12][0:8].astype(float), "2021 상세직업_군인(직업군인제외)"),
        (job_detail.values[12][9:16].astype(float), "2022 상세직업_군인(직업군인제외)"),
        (job_detail.values[13][0:8].astype(float), "2021 상세직업_기타,무직"),
        (job_detail.values[13][9:16].astype(float), "2022 상세직업_기타,무직"),

        (house.values[0][0:8].astype(float), "2021 주택형태_단독주택"), (house.values[0][9:16].astype(float), "2022 주택형태_단독주택"),
        (house.values[1][0:8].astype(float), "2021 주택형태_아파트"), (house.values[1][9:16].astype(float), "2022 주택형태_아파트"),
        (house.values[2][0:8].astype(float), "2021 주택형태_연립주택,빌라,다세대주택"),
        (house.values[2][9:16].astype(float), "2022 주택형태_연립주택,빌라,다세대주택"),
        (house.values[3][0:8].astype(float), "2021 주택형태_비거주용건물내의주택"),
        (house.values[3][9:16].astype(float), "2022 주택형태_비거주용건물내의주택"),
        (house.values[4][0:8].astype(float), "2021 주택형태_기타"), (house.values[4][9:16].astype(float), "2022 주택형태_기타"),

        (family.values[0][0:8].astype(float), "2021 가족구성_1인가구"),
        (family.values[0][9:16].astype(float), "2022 가족구성_1인가구"),
        (family.values[1][0:8].astype(float), "2021 가족구성_1세대가구"),
        (family.values[1][9:16].astype(float), "2022 가족구성_1세대가구"),
        (family.values[2][0:8].astype(float), "2021 가족구성_2세대가구"),
        (family.values[2][9:16].astype(float), "2022 가족구성_2세대가구"),
        (family.values[3][0:8].astype(float), "2021 가족구성_3세대가구"),
        (family.values[3][9:16].astype(float), "2022 가족구성_3세대가구"),
        (family.values[4][0:8].astype(float), "2021 가족구성_기타"), (family.values[4][9:16].astype(float), "2022 가족구성_기타"),

        (family_num.values[0][0:8].astype(float), "2021 가구원수_1인가구"),
        (family_num.values[0][9:16].astype(float), "2022 가구원수_1인가구"),
        (family_num.values[1][0:8].astype(float), "2021 가구원수_2인가구"),
        (family_num.values[1][9:16].astype(float), "2022 가구원수_2인가구"),
        (family_num.values[2][0:8].astype(float), "2021 가구원수_3인이상가구"),
        (family_num.values[2][9:16].astype(float), "2022 가구원수_3인이상가구"),

        (relation.values[0][0:8].astype(float), "2021 가구주와의관계_가구주"),
        (relation.values[0][9:16].astype(float), "2022 가구주와의관계_가구주"),
        (relation.values[1][0:8].astype(float), "2021 가구주와의관계_배우자"),
        (relation.values[1][9:16].astype(float), "2022 가구주와의관계_배우자"),
        (relation.values[2][0:8].astype(float), "2021 가구주와의관계_자녀"),
        (relation.values[2][9:16].astype(float), "2022 가구주와의관계_자녀"),
        (relation.values[3][0:8].astype(float), "2021 가구주와의관계_자녀의배우자"),
        (relation.values[3][9:16].astype(float), "2022 가구주와의관계_자녀의배우자"),
        (relation.values[4][0:8].astype(float), "2021 가구주와의관계_손자.녀,그배우자"),
        (relation.values[4][9:16].astype(float), "2022 가구주와의관계_손자.녀,그배우자"),
        (relation.values[5][0:8].astype(float), "2021 가구주와의관계_부모(배우자부모포함)"),
        (relation.values[5][9:16].astype(float), "2022 가구주와의관계_부모(배우자부모포함)"),
        (relation.values[6][0:8].astype(float), "2021 가구주와의관계_형제자매,그배우자"),
        (relation.values[6][9:16].astype(float), "2022 가구주와의관계_형제자매,그배우자"),
        (relation.values[7][0:8].astype(float), "2021 가구주와의관계_기타친인척"),
        (relation.values[7][9:16].astype(float), "2022 가구주와의관계_기타친인척"),
        (relation.values[8][0:8].astype(float), "2021 가구주와의관계_동거인"),
        (relation.values[8][9:16].astype(float), "2022 가구주와의관계_동거인"),
]

for data, title in data_and_titles:
    wedges, texts, autotexts = plt.pie(data,
                                       autopct=lambda pct: func(pct, data),
                                       textprops=dict(color="w"))

    plt.setp(autotexts, size=8, weight="bold")

    plt.legend(wedges,
               ["TV 홈쇼핑 - 전용 앱 구매 (%)", "TV 홈쇼핑 - 쇼핑몰 홈페이지/카페 등 인터넷 접속을 통한 온라인구매 (%)", "국내 온라인 쇼핑몰 (%) - 전용 앱 구매 (%)",
                "국내 온라인 쇼핑몰 (%) - 쇼핑몰 홈페이지/카페 등 인터넷 접속을 통한 온라인구매 (%)", "해외직구 (%) - 전용 앱 구매 (%)",
                "해외직구 (%) - 쇼핑몰 홈페이지/카페 등 인터넷 접속을 통한 온라인구매 (%)", "개인 간 거래 (%) - 전용 앱 구매 (%)",
                "개인 간 거래 (%) - 쇼핑몰 홈페이지/카페 등 인터넷 접속을 통한 온라인구매 (%)"],
               loc="center left",
               bbox_to_anchor=(1, 0, 0.5, 1))

    plt.xticks(rotation=90)
    plt.title(title)
    plt.savefig(f'{title}.png', bbox_inches='tight')
    plt.show()

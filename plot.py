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
sex = data.iloc[2:3, 0:25]

# 사례수 삭제
sex = sex.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(sex)

# 연령
age = data.iloc[4:10, 0:25]

# 사례수 삭제
age = age.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(age)

# 월평균소득
income = data.iloc[11:18, 0:25]

# 사례수 삭제
income = income.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(income)

# 학력
education = data.iloc[19:23, 0:25]

# 사례수 삭제
education = education.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(education)

# 지역
location = data.iloc[24:40, 0:25]

# 사례수 삭제
location = location.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)
print(location)

# 종사상지위
job = data.iloc[43:47, 0:25]

# 사례수 삭제
job = job.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)

print(job)

# 상세직업
job_detail = data.iloc[48:61, 0:25]

# 사례수 삭제
job_detail = job_detail.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)

print(job_detail)

# 주택형태
house = data.iloc[62:66, 0:25]

# 사례수 삭제
house = house.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7', ],
        axis=1)

print(house)

# 가족구성
family = data.iloc[67:71, 0:25]

# 사례수 삭제
family = family.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7'],
        axis=1)

print(family)

# 가구원수
family_num = data.iloc[72:74, 0:25]

# 사례수 삭제
family_num = family_num.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7'],
        axis=1)

print(family_num)

# 가구주와의관계
relation = data.iloc[75:83, 0:25]

# 사례수 삭제
relation = relation.drop(
        ['사례수 (명)', '사례수 (명).1', '사례수 (명).2', '사례수 (명).3', '사례수 (명).4', '사례수 (명).5', '사례수 (명).6', '사례수 (명).7'],
        axis=1)

print(relation)


def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))  # round: 반올림, sum: array 다 더하기
    return "{:.1f}%\n원본: {:d}%".format(pct, absolute)


# all, sex, age, income, education, job, job_detail, house, family, family_num, relation

data_and_titles = [
        (all.values[0][0:8].astype(float), "2021 전체"), (all.values[0][9:16].astype(float), "2022 전체"),
        (sex.values[0][0:8].astype(float), "2021 성별"), (sex.values[0][9:16].astype(float), "2022 성별"),
        (age.values[0][0:8].astype(float), "2021 연령"), (age.values[0][9:16].astype(float), "2022 연령"),
        (income.values[0][0:8].astype(float), "2021 월평균소득"), (income.values[0][9:16].astype(float), "2022 월평균소득"),
        (education.values[0][0:8].astype(float), "2021 학력"), (education.values[0][9:16].astype(float), "2022 학력"),
        (location.values[0][0:8].astype(float), "2021 지역"), (location.values[0][9:16].astype(float), "2022 지역"),
        (job.values[0][0:8].astype(float), "2021 종사상지위"), (job.values[0][9:16].astype(float), "2022 종사상지위"),
        (job_detail.values[0][0:8].astype(float), "2021 상세직업"), (job_detail.values[0][9:16].astype(float), "2022 상세직업"),
        (house.values[0][0:8].astype(float), "2021 주택형태"), (house.values[0][9:16].astype(float), "2022 주택형태"),
        (family.values[0][0:8].astype(float), "2021 가족구성"), (family.values[0][9:16].astype(float), "2022 가족구성"),
        (family_num.values[0][0:8].astype(float), "2021 가구원수"), (family_num.values[0][9:16].astype(float), "2022 가구원수"),
        (relation.values[0][0:8].astype(float), "2021 가구주와의관계"),
        (relation.values[0][9:16].astype(float), "2022 가구주와의관계"),

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
    plt.savefig(f'{title}.png')
    plt.show()

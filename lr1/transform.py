import pandas as pd
import random

data = pd.read_csv('drug_consumption.csv')


def map_one(age):
    if age == -0.95197:
        return random.randint(18, 25)
    elif age == -0.07854:
        return random.randint(25, 35)
    elif age == 0.49788:
        return random.randint(35, 45)
    elif age == 1.09449:
        return random.randint(45, 55)
    elif age == 1.82213:
        return random.randint(55, 65)
    else:
        return random.randint(65, 80)


data['Age'] = data['Age'].map(map_one)

gender_col = {
    0.48246: False,
    -0.48246: True
}
data['Gender'] = data['Gender'].replace(gender_col)

education_col = {
    -2.43591: 'Left School Before 16 years',
    -1.73790: 'Left School at 16 years',
    -1.43719: 'Left School at 17 years',
    -1.22751: 'Left School at 18 years',
    -0.61113: 'Some College,No Certificate Or Degree',
    -0.05921: 'Professional Certificate/ Diploma',
    0.45468: 'University Degree',
    1.16365: 'Masters Degree',
    1.98437: 'Doctorate Degree',
}
data['Education'] = data['Education'].replace(education_col)

country_col = {
    -0.09765: 'Australia',
    0.24923: 'Canada',
    -0.46841: 'New Zealand',
    -0.28519: 'Other',
    0.21128: 'Republic of Ireland',
    0.96082: 'UK',
    -0.57009: 'USA'
}
data['Country'] = data['Country'].replace(country_col)

ethnicity_col = {
    -0.50212: 'Asian',
    -1.10702: 'Black',
    1.90725: 'Mixed-Black/Asian',
    0.12600: 'Mixed-White/Asian',
    -0.22166: 'Mixed-White/Black',
    0.11440: 'Other',
    -0.31685: 'White'
}
data['Ethnicity'] = data['Ethnicity'].replace(ethnicity_col)

data.to_csv('drug_consumption_transformed.csv', index=False)

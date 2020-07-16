import pandas as pd  ### import = import library
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

disneyData = pd.read_csv("disney_movies_total_gross.csv")
####change our columns names
disneyData.rename(columns={'movie_title': "movieTitle", "release_date": "releaseDate", "MPAA_rating": "rating",
                           "total_gross": "totalGross", 'inflation_adjusted_gross': 'inflationGross'}, inplace=True)

###redeclare several variables as catagories
# change this collum = as catagory(dataFrame["column"]
disneyData["genre"] = pd.Categorical(disneyData["genre"])  ## telling python disney data is to become catagorical data
disneyData["rating"] = pd.Categorical(disneyData["rating"])
disneyData["totalGross"] = disneyData["totalGross"].astype(str)  # convert to string to strip
disneyData['totalGross'] = disneyData['totalGross'].str.replace(',', '')  # strip
disneyData['totalGross'] = disneyData['totalGross'].str.replace('$', '')  # strip
disneyData['inflationGross'] = disneyData['inflationGross'].astype(str)  # turn to string to strip
disneyData['inflationGross'] = disneyData['inflationGross'].str.replace(',', '')  # strp
disneyData['inflationGross'] = disneyData['inflationGross'].str.replace('$', '')  # strip
disneyData['inflationGross'] = disneyData['inflationGross'].astype(float)  # turn to float now datas numerical
disneyData["totalGross"] = disneyData["totalGross"].astype(float)  ##turn to float
disneyData['releaseDate'] = disneyData['releaseDate'].astype(str)
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Jan', '01')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Feb', '02')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Mar', '03')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Apr', '04')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('May', '05')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Jun', '06')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Jul', '07')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Aug', '08')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Sep', '09')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Oct', '10')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Nov', '11')  # strip
disneyData['releaseDate'] = disneyData['releaseDate'].str.replace('Dec', '12')  # strip
disneyData["movieTitle"] = pd.Categorical(disneyData["movieTitle"])
disneyData['releaseDate'] = pd.to_datetime(disneyData['releaseDate'], infer_datetime_format=True)
print(disneyData.dtypes)


####function to get a bunch of count data
def summerize_data(df1):
    for column in df1.columns:
        print(column)
        if disneyData.dtypes[column] == np.object:
            print(df1[column].value_counts())
        else:
            print(df1[column].describe())

        print('\n')


# disneyData2=disneyData.sort_values('totalGross', ascending=True)
# disneyData2=disneyData.sort_values('inflationGross', ascending=True)
disneyData2 = disneyData

# print(disneyData2)

##inflated date along with the year it was made in ascending order
panderrr = disneyData.sort_values('releaseDate', ascending=True)
releaseDateandInflat = sns.lmplot(x='releaseDate', y='inflationGross', data=panderrr, fit_reg=False, hue='genre')

sns.set(font_scale=1)
##plot inflation gross data
rando = sns.lmplot(x='releaseDate', y='inflationGross', data=disneyData2, fit_reg=False, hue='movieTitle', legend=True,
                   height=10, aspect=3)
rando.set_xticklabels(rotation=90)

##plot some data without proportional adjustments
g = sns.lmplot(x="movieTitle", y="totalGross", data=disneyData2, fit_reg=False, hue='genre', legend=True, height=5,
               aspect=3)
f = sns.lmplot(x="movieTitle", y="inflationGross", data=disneyData2, fit_reg=False, hue='genre', legend=True, height=5,
               aspect=3)
g.set_xticklabels(rotation=90)
f.set_xticklabels(rotation=90)

disneyData2.groupby(['genre']).mean()
print(disneyData2.groupby(['genre']).mean())

disneyData2.groupby('genre').agg(lambda x: sum(x)).plot(kind='pie', subplots=True,
                                                        title='Gross by each genre: with inflation and without[proprtional]')

plt.show()

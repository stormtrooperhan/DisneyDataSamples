import pandas as pd ### import = import library
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


### as = renaming

disneyData = pd.read_csv("disney_movies_total_gross.csv")
print(disneyData)
print(disneyData.dtypes)





####change our columns names
disneyData.rename(columns={'movie_title':"movieTitle", "release_date":"releaseDate", "MPAA_rating":"rating", "total_gross": "totalGross", 'inflation_adjusted_gross':'inflationGross'}, inplace=True)
print(disneyData)
#####drop a row
#disneyData.drop(axis=0)
##drop a column
#disneyData=disneyData.drop(['inflation_adjusted_gross'],axis=1)
print(disneyData)

###redeclare several variables as catagories
#change this collum = as catagory(dataFrame["column"]
disneyData["genre"]=pd.Categorical(disneyData["genre"]) ## telling python disney data is to become catagorical data
disneyData["rating"]=pd.Categorical(disneyData["rating"])


disneyData["totalGross"]=disneyData["totalGross"].astype(str)
print(disneyData.dtypes)
disneyData['totalGross'] = disneyData['totalGross'].str.replace(',', '')
disneyData['totalGross'] = disneyData['totalGross'].str.replace('$', '')

disneyData['inflationGross'] = disneyData['inflationGross'].astype(str)
disneyData['inflationGross'] = disneyData['inflationGross'].str.replace(',', '')
disneyData['inflationGross'] = disneyData['inflationGross'].str.replace('$', '')

disneyData['inflationGross'] = disneyData['inflationGross'].astype(float)
disneyData["totalGross"]=disneyData["totalGross"].astype(float)

print(disneyData.dtypes)

## shows you first entries if you want a specific number put value in head eg disneyData.head(100)
print(disneyData.head())
## shows you last entries
print(disneyData.tail())


####function to get a bunch of count data
def summerize_data(df1):
    for column in df1.columns:
        print(column)
        if disneyData.dtypes[column] == np.object:
            print(df1[column].value_counts())
        else:
            print(df1[column].describe())

        print('\n')

summerize_data(disneyData)

##disneyData.plot(x='disneyData.index', y='totalGross' , kind='scatter')

disneyData2=disneyData.head(100)


fig, axs = plt.subplots(ncols=2)
g=sns.lmplot( x="movieTitle", y="totalGross", data=disneyData2, fit_reg=False ,hue='genre', legend=True)
f=sns.lmplot( x="movieTitle", y="inflationGross", data=disneyData2, fit_reg=False ,hue='genre', legend=True)


plt.legend(loc='lower right')
g.set_xticklabels(rotation=90)
f.set_xticklabels(rotation=90)
plt.show()






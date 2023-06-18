#Importing Libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the Dataset

netflix=pd.read_csv('netflix_titles.csv')


#First 10 values
netflix.head(10)

#Shape of the dataset
netflix.shape

#Print the name of columns
netflix.columns

#Check for NULL Values
netflix.isnull().sum()

#Check unique values
netflix.nunique()

#Check for Duplicate values
netflix.duplicated().sum()


#Data Visualization

#Type: Movie and TV Shows

sns.countplot(netflix['type'])
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.title('Type')

#Rating of shows and movies
sns.countplot(netflix['rating'])
sns.countplot(netflix['rating']).set_xticklabels(sns.countplot(netflix['rating']).get_xticklabels(), rotation=90, ha="right")
fig = plt.gcf()
fig.set_size_inches(13,13)
plt.title('Rating')


#Pie-chart for the Type: Movie and TV Shows
labels = ['Movie', 'TV show']
size = netflix['type'].value_counts()
colors = plt.cm.Wistia(np.linspace(0, 1, 2))
explode = [0, 0.1]
plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(size,labels=labels, colors = colors, explode = explode, shadow = True, startangle = 90)
plt.title('Distribution of Type', fontsize = 25)
plt.legend()
plt.show()


#Pie-chart for Rating
netflix['rating'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,figsize=(10,8))
plt.show()


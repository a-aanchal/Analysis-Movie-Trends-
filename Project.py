import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('mymoviedb.csv', lineterminator='\n')
print(df.head())
#viewing dataset info
print(df.info())
#exploring genres column
print(df['Genre'].head())
#check for duplicated rows
print(df.duplicated().sum())
#exploring summary statistics
print(df.describe())
#Data cleaning
print(df.head())
#casting column a
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
#confirming change
print(df['Release_Date'].dtypes)
df['Release_Date']=df['Release_Date'].dt.year
print(df['Release_Date'].dtypes)
print(df.info())
print(df.head())
#making list of column to be dropped
cols=['Overview', 'Original_Language', 'Poster_Url']
#dropping columns and confirming changes
df.drop(cols, axis=1, inplace=True)
print(df.columns)
print(df.head())
def catigorize_col(df, col, labels):
    #setting the edges to cut the column accordingly
    edges=[df[col].describe()['min'],
           df[col].describe()['25%'],
           df[col].describe()['50%'],
           df[col].describe()['75%'],
           df[col].describe()['max']]
    df[col]=pd.cut(df[col], edges, labels, duplicates='drop')
    return df
#define labels for edges
labels = ['not_popular', 'below_avg', 'average', 'popular']
#categorize column based on labels and edges
catigorize_col(df, 'Vote_Average', labels)
#confirming changes
print(df['Vote_Average'].unique())
print(df.head())
#exploring column
print(df['Vote_Average'].value_counts())
#dropping NaNs
df.dropna(inplace=True)
#confirming
print(df.isna().sum())
print(df.head())
#split the strings into lists
df['Genre']=df['Genre'].str.split(',')
#exploring the lists
df=df.explode('Genre').reset_index(drop=True)
print(df.head())
#casting column into category
df['Genre'] = df['Genre'].astype('category')
#confirming changes
print(df['Genre'].dtypes)
print(df.info())
print(df.nunique())
#setting up seaborn configurations
sns.set_style('whitegrid')
#showing stats.on genre column
print(df['Genre'].describe())
# Grouping data by release year and calculating average popularity
popularity_by_year = df.groupby('Release_Date')['Popularity'].mean().reset_index()

# Plotting

sns.lineplot(data=popularity_by_year, x='Release_Date', y='Popularity', color='#3B2F2F', linewidth=2)
plt.title('Average Popularity by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Average Popularity')
plt.grid(True)
plt.tight_layout()
plt.show()
# Create a box plot of Vote_Average by Release Year
plt.figure(figsize=(12, 6))
sns.boxplot(x='Release_Date', y='Vote_Average', data=df, palette='Set2')

# Adding title and labels
plt.title('Box Plot of Vote Average by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Vote Average')

# Rotate x labels for better readability
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

#visualizing genre column
colors=['#4287f5', '#f54291']
sns.catplot(y='Genre', data=df, kind='count',
            hue='Genre',
            palette=sns.color_palette("coolwarm", n_colors=df['Genre'].nunique()),
            legend=False)
plt.title('Genre Distribution with Mixed Colors')
plt.show()

#visualizing vote_average column
import matplotlib.pyplot as plt

# Count occurrences of each vote average category
vote_counts = df['Vote_Average'].value_counts()

# Define custom colors for the donut chart slices
custom_colors = ['#FBA8B6', '#FCD392', '#FEBFA1', '#C8E7F1']

# Pie chart (donut chart)
plt.figure(figsize=(8, 8))
plt.pie(vote_counts, labels=vote_counts.index, autopct='%1.1f%%',
        colors=custom_colors, wedgeprops={'width': 0.4})  # Creating the "hole" in the middle
plt.title('Votes Distribution (Donut Chart)')
plt.axis('equal')  # Equal aspect ratio ensures a perfect circle
plt.show()


#checking max popularity in dataset
print(df[df['Popularity']==df['Popularity'].max()])
#checking max popularity in dataset
print(df[df['Popularity']==df['Popularity'].min()])
df['Release_Date'].hist(color='#d62728')
plt.title('Release_Date column distribution')
plt.show()
           






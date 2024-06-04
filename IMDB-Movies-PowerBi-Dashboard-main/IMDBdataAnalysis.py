import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns

# Load the IMDb Top 1000 data
file_path = 'C:/Users/vikas/Downloads/IMDB-Movies-PowerBi-Dashboard-main/IMDB-Movies-PowerBi-Dashboard-main/Data/imdb_top_1000.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Display the dataframe info to understand its structure
print(df.info())

# Check for null values
print(df.isnull().sum())

# Display basic statistics of the dataframe
print(df.describe())

# Check for duplicates
print(df.duplicated().sum())

# Display the column names
print(df.columns)

# Display the datatypes of each column
print(df.dtypes)

# Display the shape of the dataframe
print(df.shape)

# Drop the 'Poster_Link' column as it is not needed for analysis
df_clean = df.drop(['Poster_Link'], axis=1)

# Convert 'Gross' to numeric, errors='coerce' will turn non-numeric values to NaN
df_clean['Gross'] = pd.to_numeric(df_clean['Gross'].str.replace(',', ''), errors='coerce')

# Drop rows with missing values in critical columns ('Certificate', 'Meta_score', 'Gross')
df_clean = df_clean.dropna(subset=['Certificate', 'Meta_score', 'Gross'])

# Removing rows with missing values in any remaining columns
df_clean = df_clean.dropna()

# Display the number of null values after cleaning
print(df_clean.isnull().sum())

# Verify the shape of the cleaned dataframe
print(df_clean.shape)

# Count the total number of movies per genre
genre_counts = df_clean['Genre'].value_counts()
print(genre_counts)

# Basic statistics for numeric columns
numeric_statistics = df_clean.describe()
print(numeric_statistics)

# Count the number of movies per year
movies_per_year = df_clean['Released_Year'].value_counts().sort_index()
print(movies_per_year)

# Calculate the average IMDb rating per genre
avg_rating_per_genre = df_clean.groupby('Genre')['IMDB_Rating'].mean()
print(avg_rating_per_genre)

# Save the cleaned dataframe to a new CSV file
cleaned_file_path = 'C:/Users/vikas/Downloads/IMDB-Movies-PowerBi-Dashboard-main/IMDB-Movies-PowerBi-Dashboard-main/Data/imdb_top_1000_clean.csv'
df_clean.to_csv(cleaned_file_path, index=False)

# Data Visualization

# Genre Distribution
plt.figure(figsize=(12, 6))
sns.countplot(y=df_clean['Genre'], order=genre_counts.index)
plt.title('Number of Movies per Genre')
plt.xlabel('Number of Movies')
plt.ylabel('Genre')
plt.show()

# Number of Movies per Year
plt.figure(figsize=(12, 6))
sns.lineplot(x=movies_per_year.index, y=movies_per_year.values)
plt.title('Number of Movies Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45)
plt.show()

# Average IMDb Rating per Genre
plt.figure(figsize=(12, 6))
avg_rating_per_genre_sorted = avg_rating_per_genre.sort_values()
sns.barplot(x=avg_rating_per_genre_sorted.values, y=avg_rating_per_genre_sorted.index)
plt.title('Average IMDb Rating per Genre')
plt.xlabel('Average IMDb Rating')
plt.ylabel('Genre')
plt.show()

# Distribution of IMDb Ratings
plt.figure(figsize=(12, 6))
sns.histplot(df_clean['IMDB_Rating'], bins=20, kde=True)
plt.title('Distribution of IMDb Ratings')
plt.xlabel('IMDb Rating')
plt.ylabel('Frequency')
plt.show()

# Gross Earnings vs IMDb Rating
plt.figure(figsize=(12, 6))
sns.scatterplot(x='IMDB_Rating', y='Gross', data=df_clean)
plt.title('Gross Earnings vs IMDb Rating')
plt.xlabel('IMDb Rating')
plt.ylabel('Gross Earnings')
plt.show()

# %% [markdown]
# # Data Preprocessing for Brawl Stars' Datasets
# 
# * Libraries: 

# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

# %% [markdown]
# ---
# 
# </br>
# 
# # The Bests 200 Jessie's Players Dataframe
# 
# * Data import:

# %%
df_jessie = pd.read_csv("../data/raw/dataset/brawler_ranking/JESSIE_ranking.csv")

# %%
df_jessie.head(10)

# %%
df_jessie.info()

# %%
df_jessie.describe

# %%
# View the column names
print(df_jessie.columns)


# %% [markdown]
# ---
# 
# * Data Cleaning:

# %%
# Check for missing values per column
null_values = df_jessie.isnull().sum()
print("Missing values per column:\n", null_values)

# Check for total missing values in the entire dataset
total_nulls = df_jessie.isnull().sum().sum()
print(f'Total missing values in the dataset: {total_nulls}')


# %%
# Check the percentage of missing values per column
null_percentage = (df_jessie.isnull().sum() / len(df_jessie)) * 100
print("Percentage of missing values per column:\n", null_percentage)


# %%
# Replace null values in the 'club' column with "no-team-info"
df_jessie['club'] = df_jessie['club'].fillna("no-team-info")

# %%
df_jessie.head(10)

# %%
# Drop the 'Unnamed: 0' column in place
df_jessie.drop(columns=['Unnamed: 0'], inplace=True)


# %% [markdown]
# ---
# * Data normalization:

# %%
# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Normalize 'trophies' column
df_jessie['normalized_trophies'] = scaler.fit_transform(df_jessie[['trophies']])

# %%
# Normalize 'rank' column
df_jessie['normalized_rank'] = scaler.fit_transform(df_jessie[['rank']])


# %%
df_jessie.head(10)

# %% [markdown]
# ---
# 
# * Data Exportation:

# %%
# Export the DataFrame to the desired location
df_jessie.to_csv('../data/preprocessed/cleaned_jessie_ranking.csv', index=False)


# %% [markdown]
# --- 
# 
# </br>
# 
# # The bests 200 worldwide clubs dataframe
# 
# * Data import

# %%
df_club = pd.read_csv("../data/raw/dataset/global_club_info.csv")

# %%
df_club.head(10)

# %%
df_club.info()

# %%
df_club.columns

# %%
df_club.describe

# %% [markdown]
# ---
# * Data Cleaning:

# %%
# Check for missing values per column
null_values = df_club.isnull().sum()
print("Missing values per column:\n", null_values)

# Check for total missing values in the entire dataset
total_nulls = df_club.isnull().sum().sum()
print(f'Total missing values in the dataset: {total_nulls}')

# %%
# Replace null values in the 'description' column with "no-description"
df_club['description'] = df_club['description'].fillna("no-description")

# Replace null values in all other columns with "no-team-member"
df_club = df_club.fillna("no-team-member")


# %%
# Display rows where 'description' is "no-description"
df_club[df_club['description'] == 'no-description']


# %%
# Rename the column 'Unnamed: 0' to 'Rank'
df_club = df_club.rename(columns={'Unnamed: 0': 'Rank'})


# %%
df_club.head(10)

# %% [markdown]
# ---
# 
# * Normalization:

# %%
# Normalize the 'trophies' column
df_club['trophies_normalized'] = scaler.fit_transform(df_club[['trophies']])

# Normalize the 'requiredTrophies' column
df_club['requiredTrophies_normalized'] = scaler.fit_transform(df_club[['requiredTrophies']])

# %%
df_club.head()

# %% [markdown]
# --- 
# 
# * Data Exportation:

# %%
df_club.to_csv('../data/preprocessed/cleaned_club_ranking.csv', index=False)

# %% [markdown]
# ---
# 
# # Best 200 clubs in Mexico Dataframe
# 
# * Data Import:

# %%
df_mexico_clubs = pd.read_csv("../data/raw/dataset/country_club_rankings/Mexico_club_rankings.csv")


# %%
df_mexico_clubs.head(10)

# %%
df_mexico_clubs = df_mexico_clubs[df_mexico_clubs['Unnamed: 0'] != 0]  # Eliminar la fila con 'Unnamed: 0' igual a 0



# %%
# Delete the column "rank"
df_mexico_clubs.drop(columns=['rank'], inplace=True)

# Rename the column 'Unnamed: 0' to 'Rank'
df_mexico_clubs = df_mexico_clubs.rename(columns={'Unnamed: 0': 'Rank'})


# %%
df_mexico_clubs

# %% [markdown]
# ---
# 
# * Data Cleaning:

# %%
# Check for missing values per column
null_values = df_mexico_clubs.isnull().sum()
print("Missing values per column:\n", null_values)

# Check for total missing values in the entire dataset
total_nulls = df_mexico_clubs.isnull().sum().sum()
print(f'Total missing values in the dataset: {total_nulls}')

# %% [markdown]
# Fortunately, this dataset is cleaned.
# 
# ---
# 
# * Data normalization:

# %%
# Normalize the 'trophies' column
df_mexico_clubs['trophies_normalized'] = scaler.fit_transform(df_mexico_clubs[['trophies']])

# Normalize the 'requiredTrophies' column
df_mexico_clubs['member_count_normalized'] = scaler.fit_transform(df_mexico_clubs[['memberCount']])

# %%
df_mexico_clubs.head(10)

# %% [markdown]
# --- 
# 
# * Data Exportation:

# %%
df_mexico_clubs.to_csv("../data/preprocessed/cleaned_mexico_clubs_ranking.csv")

# %% [markdown]
# --- 
# 
# * Changes:
#     1. Jessie Top 200 players:
#         * Missed values replaced (No-club-info)
#         * "Unnamed: 0" column deleted
#         * "trophies" and "rank" columns scaled in min-max
#     2. Global clubs ranking:
#         * Missed values replaced (Description as "no-description" and if there had not been a team member, inserted "no-team-member")
#         * "Unnamed: 0" column replaced by "rank"
#         * "trophies" and "trophiesrequired" columns normalized by scaling min-max
#     3. Top 200 Mexican Clubs:
#         * There were neither missed nor repeated values
#         * "Unnamed: 0" column replaced by "rank"
#         * "trophies" and "trophiesrequired" columns normalized by scaling min-max



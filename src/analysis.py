# %% [markdown]
# # Data visualization and exploration.
# 
# * Notes: The datasets that you will use will be located on the folder `../data/preprocessed/`, there are three datasets you may use such as `cleaned_club_ranking.csv`, `cleaned_jessie_ranking.csv` and `cleaned_mexico_clubs_ranking.csv`
# 

# %% [markdown]
# # Import libraries

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

jessie_data = pd.read_csv('../data/preprocessed/cleaned_jessie_ranking.csv')
club_data = pd.read_csv('../data/preprocessed/cleaned_club_ranking.csv')
mexico_data = pd.read_csv('../data/preprocessed/cleaned_mexico_clubs_ranking.csv')

sns.set(style="whitegrid")

# %% [markdown]
# # Jessie Players Ranking Dataset 

# %% [markdown]
# Histogram of Trophies

# %%
plt.figure(figsize=(6, 4))
sns.histplot(jessie_data['trophies'], bins=30, kde=True)
plt.title("Distribution of Trophies Among Jessie Players")
plt.xlabel("Trophies")
plt.ylabel("Frequency")
plt.show()

# %% [markdown]
# Justification: A histogram is used to show the distribution of trophies among Jessie players. It helps to identify how evenly or unevenly the trophies are distributed.
# 
# Interpretation: If the histogram shows a concentration around certain values, it could indicate that most players are clustered in specific trophy ranges. A skewed distribution could suggest a few top players with very high trophies, and many players with lower trophies.

# %% [markdown]
# Top Clubs by Player Count

# %%
top_clubs = jessie_data['club'].value_counts().nlargest(10)
plt.figure(figsize=(6, 4))
sns.barplot(x=top_clubs.values, y=top_clubs.index, palette="viridis")
plt.title("Top Clubs by Jessie Player Count")
plt.xlabel("Number of Jessie Players")
plt.ylabel("Club")
plt.show()

# %% [markdown]
# Justification: This bar chart visualizes the clubs with the most Jessie players. It provides insights into the popularity and reach of different clubs within the Jessie player base.
# 
# Interpretation: A few clubs with large numbers of players might suggest these clubs are highly popular or have more resources, while others with fewer members could indicate newer or less active clubs.

# %% [markdown]
# Normalized Trophies vs. Normalized Rank

# %%
plt.figure(figsize= (6, 4))
sns.scatterplot(data=jessie_data, x='normalized_trophies', y='normalized_rank', hue='rank', palette="coolwarm", s=50)
plt.title("Normalized Trophies vs. Normalized Rank")
plt.xlabel("Normalized Trophies")
plt.ylabel("Normalized Rank")
plt.legend(title="Rank", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# %% [markdown]
# Justification: A scatter plot helps visualize the relationship between normalized trophies and rank, showing if higher trophies correlate with higher ranks.
# 
# Interpretation: If the plot shows an upward trend, it suggests that players with higher trophies tend to have better ranks. A random scatter could imply no strong correlation between the two variables.

# %% [markdown]
# Trophies by Player’s

# %%
plt.figure(figsize=(8,6))
sns.boxplot(x='nameColor', y='trophies', data=jessie_data)
plt.title('Box Plot of Trophies by Name Color (Jessie Players)', fontsize=14)
plt.xlabel('Name Color', fontsize=12)
plt.ylabel('Trophies', fontsize=12)
plt.xticks(rotation=90)
plt.show()

# %% [markdown]
# Justification: A box plot is used to display the distribution of trophies across different categories (here, the nameColor). It’s useful for identifying the central tendency, spread, and any potential outliers.
# 
# Interpretation: The box plot allows you to see if certain name colors correlate with higher or lower trophies. If some colors consistently have higher median trophies, it could imply a correlation between player aesthetics and their success.

# %% [markdown]
# # Clubs Ranking Dataset 

# %% [markdown]
# Club Trophy Distribution

# %%
plt.figure(figsize=(6, 4))
sns.histplot(club_data['trophies'], bins=30, kde=True)
plt.title("Distribution of Trophies Among Top Clubs")
plt.xlabel("Trophies")
plt.ylabel("Frequency")
plt.show()

# %% [markdown]
# Justification: A histogram or box plot is used to display how club trophies are distributed. It helps to understand how successful clubs are and the variation in their trophy counts.
# 
# Interpretation: A wide spread of trophy counts suggests diversity in club performance, with some clubs significantly outperforming others. A concentration around a certain range suggests that most clubs are performing at similar levels.

# %% [markdown]
# Required Trophies vs. Total Trophies

# %%
plt.figure(figsize=(6, 4))
sns.scatterplot(data=club_data, x='requiredTrophies', y='trophies', hue='Rank', palette="viridis", s=50)
plt.title("Required Trophies vs. Total Trophies in Top Clubs")
plt.xlabel("Required Trophies")
plt.ylabel("Total Trophies")
plt.legend(title="Rank", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# %% [markdown]
# Justification: This scatter plot compares the required trophies to join a club with the total trophies of that club. It helps to understand if clubs with higher required trophies also perform better.
# 
# Interpretation: If the plot shows a positive correlation, clubs with higher entry requirements tend to have more total trophies, suggesting that tougher clubs attract stronger players.

# %% [markdown]
# Roles Distribution

# %%
role_columns = [col for col in club_data.columns if 'member_' in col and '_role' in col]
roles = pd.concat([club_data[col] for col in role_columns])
role_counts = roles.value_counts()
plt.figure(figsize=(6, 4))
sns.barplot(x=role_counts.values, y=role_counts.index, palette="Blues_d")
plt.title("Distribution of Roles Among Top Club Members")
plt.xlabel("Count")
plt.ylabel("Role")
plt.show()

# %% [markdown]
# Justification: This bar chart displays the distribution of roles among the top members of the clubs, providing insights into the typical composition of successful clubs.
# 
# Interpretation: A dominant role (e.g., leaders or strategists) could suggest that most clubs are structured with specific positions to optimize performance. A more balanced distribution indicates a versatile or less role-dependent structure.

# %% [markdown]
# Normalized Trophies vs. Rank

# %%
plt.figure(figsize=(6, 4))
sns.lineplot(data=club_data, x='Rank', y='trophies_normalized')
plt.title("Normalized Trophies vs. Rank")
plt.xlabel("Rank")
plt.ylabel("Normalized Trophies")
plt.show()

# %% [markdown]
# Justification: This line plot shows how normalized trophies correlate with rank across clubs. It helps visualize the relationship between performance (normalized trophies) and ranking.
# 
# Interpretation: A line moving upward indicates that clubs with higher normalized trophies tend to achieve better ranks. Flat or erratic lines suggest no clear trend between trophies and rank.

# %% [markdown]
# Required Trophies vs. Total Trophies for Clubs

# %%
corr_matrix = club_data[['requiredTrophies', 'trophies']].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title('Heatmap of Required Trophies vs. Total Trophies (Clubs)', fontsize=16)
plt.show()

# %% [markdown]
# Justification: A heatmap helps visualize the correlation between two continuous variables, in this case, required trophies and total trophies. It can show patterns or correlations in a color-coded format.
# 
# Interpretation: A strong color correlation (either positive or negative) between the required trophies and total trophies indicates a meaningful relationship. A lack of correlation (neutral color) suggests that these variables might not be closely related.

# %% [markdown]
# # Mexico Clubs Ranking Dataset 

# %% [markdown]
# Trophy and Member Count Distributions

# %%
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
sns.histplot(mexico_data['trophies'], bins=30, kde=True, ax=ax[0])
ax[0].set_title("Distribution of Trophies in Mexican Clubs")
ax[0].set_xlabel("Trophies")

sns.histplot(mexico_data['memberCount'], bins=30, kde=True, ax=ax[1])
ax[1].set_title("Distribution of Member Count in Mexican Clubs")
ax[1].set_xlabel("Member Count")
plt.show()

# %% [markdown]
# Justification: Two histograms display the distribution of trophies and member counts among Mexican clubs. This helps understand the size and performance variability of clubs in the region.
# 
# Interpretation: Clubs with higher trophies might have fewer members, or large clubs may be less successful. The shapes of the distributions give insight into how clubs are structured in terms of achievements and size.

# %% [markdown]
# Normalized Trophies vs. Member Count

# %%
plt.figure(figsize=(6, 4))
sns.scatterplot(data=mexico_data, x='trophies_normalized', y='member_count_normalized', hue='Rank', palette="coolwarm", s=50)
plt.title("Normalized Trophies vs. Normalized Member Count in Mexican Clubs")
plt.xlabel("Normalized Trophies")
plt.ylabel("Normalized Member Count")
plt.legend(title="Rank", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# %% [markdown]
# Justification: A scatter plot shows whether clubs with more members tend to have higher normalized trophies, indicating the relationship between size and success.
# 
# Interpretation: If a positive correlation is found, larger clubs might have more success, potentially due to having more resources or players to contribute to the overall performance. A lack of correlation suggests that club size doesn’t necessarily impact performance.

# %% [markdown]
# Ranking Analysis

# %%
plt.figure(figsize=(6, 4))
sns.scatterplot(data=mexico_data, x='Rank', y='trophies_normalized', hue='memberCount', palette="viridis", s=50)
plt.title("Rank vs. Normalized Trophies in Mexican Clubs")
plt.xlabel("Rank")
plt.ylabel("Normalized Trophies")
plt.legend(title="Member Count", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# %% [markdown]
# Justification: A scatter plot shows the relationship between club rank and normalized trophies in Mexican clubs, helping analyze how performance affects ranking.
# 
# Interpretation: A positive correlation indicates that clubs with higher trophies tend to rank better. A scattered distribution might suggest that rank is not solely dependent on trophy count but may involve other factors like club activity or player contributions.

# %% [markdown]
# Trophies, Member Count, and Normalized Trophies

# %%
sns.pairplot(mexico_data[['trophies', 'memberCount', 'trophies_normalized']])
plt.suptitle('Trophies, Member Count, and Normalized Trophies (Mexico Clubs)', fontsize=14)
plt.show()

# %% [markdown]
# Justification: A pair plot shows the relationships between multiple variables and is useful for detecting correlations, trends, or clusters in a dataset with more than one numeric feature.
# 
# Interpretation: The pair plot will help identify which variables are most correlated with each other (e.g., member count and trophies) and provide insights into how these attributes relate to each other across clubs in Mexico.



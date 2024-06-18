import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine()

df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
df_wine['target'] = wine.target
print(df_wine.head())

# histogram
df_wine['alcohol'].plot(kind='hist', bins=20, title='Distribution of Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Frequency')
plt.show()

# Bar plot of Wine classes
df_wine['target'].value_counts().plot(kind='bar', title='Distribution of Wine Classes')
plt.xlabel('Class')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Box plot of Alcohol content by Wine class
df_wine.boxplot(column='alcohol', by='target')
plt.title('Alcohol Content by Wine Class')
plt.xlabel('Class')
plt.ylabel('Alcohol Content')
plt.show()

# Scatter plot of Alcohol content vs. Flavanoids
plt.scatter(df_wine['alcohol'], df_wine['flavanoids'], c=df_wine['target'], cmap='viridis')
plt.title('Alcohol Content vs. Flavanoids')
plt.xlabel('Alcohol Content')
plt.ylabel('Flavanoids')
plt.colorbar(label='Wine Class')
plt.show()

# Line chart of Alcohol content over Index
df_wine['alcohol'].plot(kind='line', title='Alcohol Content Over Index')
plt.xlabel('Index')
plt.ylabel('Alcohol Content')
plt.show()

# Line chart with two lines: Alcohol content and Malic acid content
plt.plot(df_wine['alcohol'], label='Alcohol Content')
plt.plot(df_wine['malic_acid'], label='Malic Acid Content')
plt.title('Alcohol Content vs. Malic Acid Content')
plt.xlabel('Index')
plt.ylabel('Content')
plt.legend()
plt.show()

# Line chart with markers: Alcohol content with circle markers, Malic acid content with triangle markers
plt.plot(df_wine['alcohol'], label='Alcohol Content', marker='o--')
plt.plot(df_wine['malic_acid'], label='Malic Acid Content', marker='^')
plt.title('Content Comparison with Markers')
plt.xlabel('Index')
plt.ylabel('Content')
plt.legend()
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = {
    'year': [07.00, 07.00, 07.00, 07.30, 07.30, 07.30, 08.00, 08.00, 08.00],
    'month': ['Introduction to Psychology', 'Environmental Science and Sustainability', 'World History: From Ancient Civilizations to the Modern Era'
              , 'Introduction to Psychology', 'Environmental Science and Sustainability', 'World History: From Ancient Civilizations to the Modern Era'
              , 'Introduction to Psychology', 'Environmental Science and Sustainability', 'World History: From Ancient Civilizations to the Modern Era'],
    'passengers': [20, 11, 15, 11, 2, 20, 1, 3, 17]
}
# Convert the dictionary to a pandas DataFrame
flights_data = pd.DataFrame(data)

# Pivot the data to have months on rows and years on columns
data_pivoted = flights_data.pivot(index="month", columns="year", values="passengers")

# Create the heatmap
sns.heatmap(data_pivoted, cmap="coolwarm", annot=True, fmt=".0f")

# Add a title to the plot
plt.title("Passenger Count Heatmap")

# Show the plot
plt.show()

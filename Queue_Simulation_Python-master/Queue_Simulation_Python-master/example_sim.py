import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = {
    'year': [1949, 1949, 1949, 1950, 1950, 1950, 1951, 1951, 1951],
    'month': ['January', 'February', 'March', 'January', 'February', 'March', 'January', 'February', 'March'],
    'passengers': [112, 118, 132, 115, 126, 141, 135, 148, 148]
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

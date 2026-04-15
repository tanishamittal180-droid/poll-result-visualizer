import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/cleaned_poll_data.csv")

# Count votes
counts = df['Preferred_Tool'].value_counts()

# Bar chart
sns.barplot(x=counts.index, y=counts.values)
plt.title("Tool Preference")
plt.savefig("outputs/bar_chart.png")
plt.show()

# Pie chart
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
plt.title("Vote Share")
plt.savefig("outputs/pie_chart.png")
plt.show()

# Region/Demographic analysis
sns.countplot(x='Preferred_Tool', hue='Gender', data=df)
plt.title("Gender-wise Preference")
plt.show()
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("📊 Poll Results Visualizer")

df = pd.read_csv("data/cleaned_poll_data.csv")

# Show data
if st.checkbox("Show Data"):
    st.dataframe(df)

# Bar chart
st.subheader("Tool Preference")
counts = df['Preferred_Tool'].value_counts()
st.bar_chart(counts)

# Pie chart
st.subheader("Vote Share")
fig, ax = plt.subplots()
ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
st.pyplot(fig)

# Word cloud
st.subheader("Feedback Word Cloud")
text = ' '.join(df['Feedback'].astype(str))
wordcloud = WordCloud().generate(text)

fig2, ax2 = plt.subplots()
ax2.imshow(wordcloud)
ax2.axis('off')
st.pyplot(fig2)
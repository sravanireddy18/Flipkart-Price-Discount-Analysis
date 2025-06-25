import streamlit as st
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Univariate Analysis")

# Add text
df=pd.read_csv(r"C:\Users\bsrav\INNOMATICS\INNOMATICS_NOTEBOOK\PROJECT\Flipkart_webscraping_prj\flipkart_products_cleaned1.csv")

st.subheader("📊 Price Distribution")
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], bins=20, kde=True, color="skyblue")
plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
st.pyplot(plt)


st.subheader("⭐ Rating Distribution")
plt.figure(figsize=(10, 6))
sns.violinplot(x=df['Rating'], color='green')
plt.title("Rating Distribution")
plt.xlabel("Rating")
st.pyplot(plt)


st.subheader("🎯 Discount Distribution")
plt.figure(figsize=(10, 6))
sns.barplot(x=df['Discount'].value_counts().index, y=df['Discount'].value_counts().values, color='orange')
plt.title("Discount Distribution")
plt.xlabel("Discount")
plt.ylabel("Frequency")
st.pyplot(plt)


st.subheader("🔋 Battery Capacity Distribution")
plt.figure(figsize=(10, 6))
sns.histplot(df['Battery'], kde=True, color='red')
plt.title("Battery Capacity Distribution")
plt.xlabel("Battery Capacity (mAh)")
plt.ylabel("Frequency")
st.pyplot(plt)




# Adding the button
if st.button("Click Me for the Insight"):
    st.write("""
    **Histplot Insight:**  
    The price distribution is **bimodal**, showing two distinct price peaks, likely representing different item categories.  
    Significant gaps exist between bars, especially between the two main price clusters and in higher price ranges,  
    indicating a lack of data in those intervals.  
    The distribution is slightly **right-skewed** due to some higher-priced items.
             

    **Violinplot Insight:**  
    Ratings are mostly high, clustering around 4.4, with a multimodal distribution showing distinct rating groups. 
    Few ratings are below 4.1, and the plot highlights the range and spread of ratings, indicating generally positive feedback.


    **Barplot Insight:**  
    The discount distribution is uneven, favoring specific percentages like 11, 13, 15, 25, and 27. 
    Discounts in the mid-range (around 16-20) are less frequent. 
    The chart shows a range of discounts from near 0 to 40, suggesting distinct, rather than continuous, discount strategies.


    **Histplot Insight:**  
    Battery capacities are heavily concentrated around 5000 mAh, with a smaller peak around 4500 mAh. 
    Almost all batteries fall within these two ranges, showing a strong preference for high-capacity batteries. 
    A tiny fraction has very low capacity.         
    """)


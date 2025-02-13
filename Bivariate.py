import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
st.title("Bivariate Analysis")

# Add text
df=pd.read_csv(r"C:\Users\bsrav\INNOMATICS\INNOMATICS_NOTEBOOK\PROJECT\Flipkart_webscraping_prj\flipkart_products_cleaned1.csv")

st.subheader("💰 Price vs ⭐ Rating")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Price', y='Rating', hue='Brand', palette='viridis')
plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Rating")
st.pyplot(plt)


st.subheader("💸 Price vs 🎯 Discount")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Price', y='Discount', hue='Brand', palette='coolwarm')
plt.title("Price vs Discount")
plt.xlabel("Price")
plt.ylabel("Discount (%)")
st.pyplot(plt)


# Adding the button
if st.button("Click Me for the Insight"):
    st.write("""
    **Plot 1 Insight:**  
    Price and rating show little correlation. 
    High ratings exist across all price points, and similar prices don't guarantee similar ratings. 
    Clusters suggest brand trends. Price doesn't reliably predict phone rating

    **Plot 2 Insight:**           
    Discount percentage shows no clear relationship with phone price. 
    High discounts appear across various price ranges, and most discounts are low regardless of price. 
    Brand plays a bigger role than price in determining discount amount.
    """)

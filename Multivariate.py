import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
st.title("Multivariate Analysis")

# Add text
df=pd.read_csv(r"C:\Users\bsrav\INNOMATICS\INNOMATICS_NOTEBOOK\PROJECT\Flipkart_webscraping_prj\flipkart_products_cleaned1.csv")

st.subheader("📊 Correlation Heatmap")
plt.figure(figsize=(12, 8))
corr_matrix = df[['Price', 'Rating', 'Discount', 'Battery']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap of Price, Rating, Discount, and Battery")
st.pyplot(plt)


# Adding the button
if st.button("Click Me for the Insight"):
    st.write("""
    **Insight:**  
    Price moderately correlates with Rating (0.66), negatively with Discount (-0.59), and strongly negatively with Battery (-0.79).
    Rating correlates negatively with Discount (-0.64) and weakly with Battery (-0.23).
    Discount weakly correlates with Battery (0.23). Price is the strongest predictor.
    """)
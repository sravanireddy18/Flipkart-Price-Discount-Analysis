import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
st.title("Categorical Analysis")

# Add text
df=pd.read_csv(r"C:\Users\bsrav\INNOMATICS\INNOMATICS_NOTEBOOK\PROJECT\Flipkart_webscraping_prj\flipkart_products_cleaned1.csv")
st.subheader("🏷️ Brand Distribution")
plt.figure(figsize=(10, 6))
sns.countplot(x='Brand', data=df, palette='Set2')
plt.title("Brand Distribution")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(plt)


# Adding the button
if st.button("Click Me for the Insight"):
    st.write("""
    **Insight:**  
    Motorola dominates the brand distribution. 
    Vivo is second most common. CMF, Samsung, POCO, OPPO, and Redmi have moderate representation. 
    Realme, Infinix, and Apple are barely present.
    """)

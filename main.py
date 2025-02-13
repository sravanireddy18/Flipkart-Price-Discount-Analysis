import streamlit as st
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Flipkart Price & Discount Analysis: Unveiling the Impact on Sales and Customer Satisfaction")

# Add text
df=pd.read_csv(r"C:\Users\bsrav\INNOMATICS\INNOMATICS_NOTEBOOK\PROJECT\Flipkart_webscraping_prj\flipkart_products_cleaned1.csv")
st.subheader("🔍 Preview of Dataset")
st.write(df.head(10))

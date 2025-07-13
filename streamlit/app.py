
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



## Title of the application

st.title("Title: : Welcome to streamlit")

## Markdown Features

st.markdown("# Markdown header features :")

st.markdown("### Use ### for small header")
st.markdown("# Use # for large header")
st.markdown("## Use ## for medium header")


## Markdown text features

st.markdown("# Markdown text features : ")

st.markdown("This is markdown *italic* text")
st.markdown("This is markdown **bold** text")
st.markdown("This is ***bold and italic*** text")

## Simple text

st.markdown("# Simple text :")
st.write("Hi ! Hope you are doing well. This it the st.write feature of streamlit where you can write any text content")


## Browse and load a csv file 

st.markdown("# File Uploader :")

csv_file = st.file_uploader("Load a csv file")


if csv_file:

    ## Read the csv file as dataframe using pandas

    df=pd.read_csv(csv_file)
    df_sorted=df.sort_values("Month")

    ## Preview dataframe

    st.dataframe(df)

    ## Plots in streamlit

    st.markdown("## Sales and profit Trends using Line chart")

    ## Using radio button select the car

    car=st.radio("Select using st.radio button", options=["Tiago", "Nexon"])


    df_car=df[df["Product"]==car]

    st.dataframe(df_car)

    
    if st.button("Sales chart using line chart"):

        plt.figure()
        plt.plot(df_car["Month"], df_car["Sales"])
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.title("Sales Trend")
        st.pyplot(plt)

    if st.button("Profit chart using line chart"):

        plt.figure()
        plt.plot(df_car["Month"], df_car["Profit"])
        plt.xlabel("Month")
        plt.ylabel("Profit")
        plt.title("Profit Trend")
        st.pyplot(plt)


    ## Monthwise sales/profit comparison

    st.markdown("## Monthwise sales/profit comparison")

    sales_profit=st.selectbox("Select using st.selectbox dropdown", options=["Sales", "Profit"])

    # Pivot the data for plotting

    pivot_df = df.pivot(index='Month', columns='Product', values=sales_profit)

    if st.button("Monthwise comparsion using bar chart"):

        plt.figure()
        pivot_df.plot(kind='bar', figsize=(8, 5))
        plt.xlabel("Month")
        plt.ylabel(sales_profit)
        plt.title("Monthwise comparison using bar chart")
        st.pyplot(plt)

    ## Sales share by piechart

    st.markdown("## Sales by piechart")

    # Group by product and sum sales
    sales_by_product = df.groupby('Product')['Sales'].sum()

    if st.button("pie chart"):

        plt.figure()
        plt.pie(sales_by_product.values, labels=sales_by_product.index, autopct='%1.1f%%', startangle=90)
        plt.title('Contribution of Total Sales by Product')
        st.pyplot(plt)
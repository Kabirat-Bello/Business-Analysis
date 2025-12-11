import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# reading the csv file.
df = pd.read_csv("Business_sales_EDA.csv", sep =";", index_col= "Product ID")
# st.dataframe(df)
# cleaning the dataset
df= df.drop(columns=['Product Category', 'brand', 'url', 'name', 'description', 'currency'])
# drop the nan value
df.dropna(inplace = True)

# creating a function the filter the data set based on the selected value from a column.
def filter_data(df, column, item):
    """
    This filter the entire dataset based on the select column and item.

    Parameter 
        df: Dataframe
        Column: The column name
        item: An element in the column.
    Return
        Dataframe.
    """
    if column is not None:
        if item is not None:
            # filter the dataset
            filter_df = df[df[column]==item]
            return filter_df
    return df

# configuring the side bar
sidebar = st.sidebar
sidebar.header("Configure the Dataset")
sidebar.write("Tweak the Data set in the way that suits you")
# Choose the column.
columns = df.select_dtypes("O").columns
column = sidebar.selectbox("Choose a column", columns, index = None)
# Get the item.
if column is not None:
    items = df[column].unique().tolist()
    item = sidebar.selectbox("Choose an item to filter by", items, index= None)
else:
    item = None

filtered_df= filter_data(df,column, item)
# application of the header
if column is not None:
    st.header(f"Business sales Analysis for {column.capitalize()}", divider= "gray")
else:
    st.header("Business sales Analysis", divider= "gray")

# configure the metrics in 3 columns
col1, col2, col3 = st.columns(3)
# adding metric to each column
col1.metric(label = "Total Price", value= f'${round(filtered_df["price"].sum()/1000, 2)} K', border= True)
col2.metric(label = "Total Sales Price", value= f'{round(filtered_df["Sales Volume"].sum()/1000000,2)} M', border= True)
col3.metric(label = "Total Records", value=filtered_df.shape[0], border = True)

# display the dataframe
st.dataframe(filtered_df)

# visualization
vis1 = filtered_df["origin"].value_counts().sort_values(ascending = True)
vis2 = filtered_df.groupby("origin")["price"].mean().sort_values()
if item is not None:
    st.write(px.bar(vis1, orientation= "h", title = f'Distribution of {item} across origin'))
    st.write(px.bar(vis2, orientation= "h", title = f'Mean Price Distribution across origin'))
    





    








            

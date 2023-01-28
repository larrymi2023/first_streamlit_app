import streamlit
import pandas



streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kyle, Spinach & Rocket smoothie')
streamlit.text('🐔Hard-bioled free-range egg')
streamlit.text('🥑Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


import streamlit
import pandas



streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kyle, Spinach & Rocket smoothie')
streamlit.text('🐔Hard-bioled free-range egg')
streamlit.text('🥑Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strewberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


import streamlit

streamlit.title( 'My Parents New Healthy Diner' )

streamlit.header( 'Breakfast Favorites' )
streamlit.text( '🥣 Omega 3 & Blueberry Oatmeal' )
streamlit.text( '🥗 Kale, Spinich & Rocket Smoothie' )
streamlit.text( '🐔 Hard-boiled Free-range Egg')
streamlit.text( '🥑🍞 Avacado Toast' )
   
import Pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

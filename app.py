import streamlit as st

st.write("""
# Pick the largest number

This app predicts the largest out of 3 numbers
""")

st.header('User Input')

def user_input_features():
  num1 = st.number_input("Enter first number: ")
  num2 = st.number_input("Enter second number: ")
  num3 = st.number_input("Enter third number: ")

largest_number = max(num1, num2, num3)
print("The largest number is:", largest_number)

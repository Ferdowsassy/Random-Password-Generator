import streamlit as st
import random
import string
import pyperclip

st.title("Random Password Generator")

length = st.number_input("Password Length:", min_value=1, step=1)

uppercase = st.checkbox("Include Uppercase Letters")
numbers = st.checkbox("Include Numbers")
special_chars = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    
    st.text_input("Generated Password:", password, disabled=True)
    
    copy_button = st.button("📋 Copy Password")
    if copy_button:
        pyperclip.copy(password)
        st.success("Copied to clipboard!")

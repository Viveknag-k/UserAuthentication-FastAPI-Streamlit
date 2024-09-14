
import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

st.title("Authentication System")
page = st.selectbox("Choose your action:", ["Login", "Sign Up"])

if page=="Sign Up":
    
    st.subheader("Sign Up")

    # User inputs for sign-up
    new_username = st.text_input("Enter a new username:")
    new_password = st.text_input("Enter a new password:", type="password")
    
    if st.button("Sign Up"):
        if new_username and new_password:
            signup_response= requests.post(f"{API_URL}/signup/", json={"username":new_username,
                                                                "password":new_password})
            if signup_response.status_code==200:
                st.success("Signed Up successfully. You can sign in now.")
            elif signup_response.status_code==400:
                st.error("Username Alredy Exists")
            else:
                st.error("Something went wrong")
        else:
            st.error("Please fill the details")
elif page=="Login":
    st.subheader("Login")
    
    username=st.text_input("Enter username:")
    password=st.text_input("Enter password:",type="password")
    
    if st.button("Login"):
        if username and password:
            login_response=requests.post(f"{API_URL}/validate/", json={"username":username,
                                                                       "password":password})
            if login_response.status_code==200:
                st.success("Logged in successfully")
            else:
                st.error("Invalid Credentials")
        else:
            st.error("Please fill the details")
            
    
    
    
    
    
    
    
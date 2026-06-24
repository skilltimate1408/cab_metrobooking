import streamlit as st
st.title("Student Registration")
name=st.text_input("Full Name")
email=st.text_input("Email")
mobile=st.text_input("Mobile Number")
course=st.selectbox("Select Course",
           ["Python","Java","AI"])
if st.button("Registration"):
    if not name or not email or not mobile:
        st.warning("please fill all the details")
    else:
        st.success("Registration Done!")
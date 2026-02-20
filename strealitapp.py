import streamlit as st
from logic.career_engine import (
    career_after_10th,
    career_after_12th,
    career_after_engineering,
    medical_specialization,
    govt_careers
)

st.set_page_config(page_title="Career Path AI")

st.title("🎓 Career Path AI")
st.write("Your real-time career guide")

option = st.selectbox(
    "Choose your stage",
    ["After 10th", "After 12th", "Engineering", "Medical", "Explore Careers"]
)

if option == "After 10th":
    choices = st.multiselect(
        "Select interests",
        ["Maths", "Science", "Arts", "Commerce", "Technology", "Medical", "Design", "Business"]
    )
    if st.button("Show Careers"):
        result = career_after_10th(",".join(choices))
        st.success(result)

elif option == "After 12th":
    stream = st.selectbox("Choose stream", ["Science", "Commerce", "Arts"])
    if st.button("Show Careers"):
        st.success(career_after_12th(stream))

elif option == "Engineering":
    branch = st.selectbox("Branch", ["CSE", "ECE", "MECH", "CIVIL"])
    interest = st.selectbox("Interest", ["Software", "Core", "Research"])
    if st.button("Show Careers"):
        st.success(career_after_engineering(branch, interest))

elif option == "Medical":
    interest = st.selectbox("Interest", ["Clinical", "Research", "Administration"])
    if st.button("Show Careers"):
        st.success(medical_specialization(interest))

elif option == "Explore Careers":
    interest = st.selectbox("Interest", ["Government", "Private", "Defense"])
    if st.button("Show Careers"):
        st.success(govt_careers(interest))
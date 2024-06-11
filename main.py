import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Jaishree Daulagar")
    content = """
    I have 1 year python Programming experience and possess Master's degree in Computer Science with University Distinction 
    and Bachelor's degree in Electrical and Electronics Engineering.  In addition to Python, I have experience 
    in Business Intelligence tools such as Informatica, Business Objects, Crystal Reports, SSIS, Cognos & 
    Tableau. 
      
    """
    st.info(content)
    content2 = """ 
    Below you can find some of the apps I have built in Python. Feel Free to contact me! 
    """
st.write(content2)
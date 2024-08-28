import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Jaishree Daulagar")
    content = """
    I have 6 years experience as "Senior Software Engineer". Python programming experience as well and possess Master's degree in Computer Science with University Distinction 
    and Bachelor's degree in Electrical and Electronics Engineering.  In addition to Python, Pandas, Numpy, SciPy, Matplotlib, Jupyter, Machine Learning, SciKit-learn, TensorFlow, PyTorch, I have experience 
    in SQL, Hadoop, Business Intelligence tools such as Informatica, Alteryx, SSIS, Business Objects, Crystal Reports,  ITIL (Service Now Support), Cognos,& 
    Tableau, Airflow & Control-M. Worked in Banking, Capital Market, Health Insurance, Pharmaceutical, Electronics and Leasing Industry. 
      
    """
    st.info(content)
    content2 = """ 
    Below you can find some of the apps I have built in Python. Feel Free to contact me! 
    """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:5].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
       # st.write("[Source Code](https://pythonhow.com)")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[5:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
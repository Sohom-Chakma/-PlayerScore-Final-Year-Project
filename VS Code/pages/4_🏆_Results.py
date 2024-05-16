import streamlit as st
import pandas as pd



bd= pd.read_csv("Standardized Data.csv").sort_values(by="PlayerScore", ascending= False)

# setting page configurations
st.set_page_config(
    page_title="Results",
    page_icon=":soccer:",
    layout='wide')

#creating sidebar with caption
st.sidebar.success("Explore my project!")

st.title("Results")


tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Ballon D'Or", "FIFA The Best", "PFA", "La Liga Awards", "Serie A Footballer of the Year", "Ligue 1 Player of the Year", "Bundesliga Player of the Year"])

with tab1:
   st.header("Ballon D'Or")
   st.image("goat-7-min.jpg", width=200)
   st.write(bd['Player'].head(1))
   st.dataframe(bd)

with tab2:
   st.header("FIFA The Best")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("Yashin Trophy")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with tab4:
   st.header("PFA")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   
with tab5:
   st.header("La Liga Awards")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
      
with tab6:
   st.header("La Liga Awards")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
      
with tab7:
   st.header("La Liga Awards")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
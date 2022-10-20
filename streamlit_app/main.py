import streamlit as st
from streamlit_option_menu import option_menu
import db

# horizontal Menu
selected2 = option_menu(None, ["Search", "Home", "About"],
icons=['search', 'house', 'cloud-upload'],
menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Home":
    st.write('you are at Home')
elif selected2 == "About":
    st.write('you are at About')
elif selected2 == "Search":
    with st.form("search_form"):
        query = st.text_input('Search')
        submitted = st.form_submit_button("Go")
    if submitted:
            st.write(f'you searched for {query}')
            resp = db.query()
            for item in resp:
                st.write(item)
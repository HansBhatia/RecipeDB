import streamlit as st
from streamlit_option_menu import option_menu
import db
from queries import *
import auth_lib
from db_schema_helpers import *
import time

col1, col2, col3 = st.columns(3)
with col1:
    " "
image = Image.open('cooking.jpeg')
with col2:
    st.image(image, caption='') 
with col3:
    " "

st.markdown("<h1 style='text-align: center; color: black;'>ReciepeDB</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: grey;'>Search for ingredients or recipes bellow! </h2>", unsafe_allow_html=True)


# horizontal Menu
selected2 = option_menu(None, ["Search", "Popular Recipes", "About", "Login/SignUp"],
icons=['search', 'star', 'cloud-upload', 'user'],
menu_icon="cast", default_index=0, orientation="horizontal")

# check logged in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['user_obj'] = {}

if not(st.session_state['logged_in']):
    st.info('Please login to rate the recipes!', icon="ℹ️")
if selected2 == "Home":
    st.write('you are at Home')
elif selected2 == "About":
    # prints out the md file
    with open('../README.md') as f:
        st.markdown(f.read())
elif selected2 == "Search":
    with st.form("search_form"):
        query = st.text_input('Search')
        genre = st.radio("Type", ('By Ingredients', 'By Recipe'))
        submitted = st.form_submit_button("Go")
    if submitted:
        with st.spinner('Searching...'):
            time.sleep(3)
        st.success('Done!')
        st.write(f'you searched for {query}')
        search_items = list(map(lambda x: x.strip(), query.split(',')))
        query_string = ''
        resp = []
        if genre == 'By Ingredients':
            # search by ingredient
            # construct query
            query_string = ''
            for item in search_items:
                sub_q = food_to_recipe_id.format(f"'{item}'")
                if query_string != '':
                    query_string += ' INTERSECT ' + sub_q
                else:
                    query_string = sub_q
            # get recipe objects
            query_string = recipe_from_id.format(f'({query_string})')
            resp = db.query(query_string)
        else:
            # search by ingredient
            # construct query
            query_string = ''
            for item in search_items:
                sub_q = recipe_to_recipe_id.format(f"'{item}'")
                if query_string != '':
                    query_string += ' UNION ' + sub_q
                else:
                    query_string = sub_q
            # get recipe objects
            query_string = recipe_from_id.format(f'({query_string})')
            resp = db.query(query_string)
        ###PRINT POSTS###
        rec_table_to_posts(resp)
elif selected2 == "Login/SignUp":
    if st.session_state['logged_in']:
        st.write('You are Logged In!')
        if st.button('Logout'):
            st.session_state['logged_in'] = False
            st.session_state['user_obj'] = {}
            st.experimental_rerun()
    else:
        LoginSignUpT = st.radio("Type", ('Login', 'SignUp'))      
        if LoginSignUpT == 'Login':
            with st.form("search_form"):
                username = st.text_input('Username')
                password = st.text_input("Password", type="password", key="password")
                submitted = st.form_submit_button("Sign In")
            if submitted:
                # verify
                user_obj = auth_lib.validatePassword(username, password)
                if user_obj:
                    st.session_state['logged_in'] = True
                    st.session_state['user_obj'] = user_obj
                    st.success('Done!')
                    st.experimental_rerun()
                else:
                    st.error('Invalid Credentials')
        elif LoginSignUpT == 'SignUp':
            with st.form("detail_form"):
                username = st.text_input('Username')
                email = st.text_input('email')
                password = st.text_input("Password", type="password", key="password")
                password2 = st.text_input("Re-enter Password", type="password", key="password2")
                submitted = st.form_submit_button("Sign Up")
            if submitted:
                # verify
                if password != password2:
                    st.error('Passwords do not match!')
                else:
                    # TODO fix the signup insert issue
                    u_obj = auth_lib.createUser(username, email, password, 'test.url')
                    print(u_obj)
                    if u_obj != []:
                        st.success('Done')
                        LoginSignUpT = 'Login'
                        st.experimental_rerun()
                    else:
                        st.error('Error In Account Creation')
elif selected2 == "Popular Recipes":
    count = st.slider('Browse the top recipes:', 1, 100, 5)
    
    query_string = get_top_n_recipes.format(count)
    second_query_string = get_unrated_recipes
    tresp = db.query(query_string)
    remaining = count - len(tresp)
    tresp2 = db.query(second_query_string.format(remaining))
    resp = tresp + tresp2
    ###PRINT POSTS### MIGHT BE UNORDERED TODO
    rec_table_to_posts(resp, add_index=True)
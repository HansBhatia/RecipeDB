import streamlit as st
from streamlit_option_menu import option_menu
import db
from queries import *
from PIL import Image

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
        genre = st.radio("Type", ('By Ingredients', 'By Recipe'))
        submitted = st.form_submit_button("Go")
    if submitted:
        st.write(f'you searched for {query}')
        search_items = list(map(lambda x: x.strip(), query.split(',')))
        query_string = ''
        resp = []
        if genre == 'By Ingredients':
            # search by ingredient
            # construct query
            query_string = ''
            for item in search_items:
                sub_q = food_to_recipe_id.format(item)
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
                sub_q = recipe_to_recipe_id.format(item)
                if query_string != '':
                    query_string += ' UNION ' + sub_q
                else:
                    query_string = sub_q
            # get recipe objects
            query_string = recipe_from_id.format(f'({query_string})')
            resp = db.query(query_string)
        ###PRINT POSTS###
        for item in resp:
            col1, col2 = st.columns([2, 2])
            with col1:
                # col_name: image
                image = Image.open('coconut.jpeg')
                new_image = image.resize((600, 400))
                st.image(new_image)
                #st.image('https://post.healthline.com/wp-content/uploads/2020/01/coconut-holding-fruit-1200x628-facebook.jpg')
            with col2:
                # col_name: name
                st.text(item[1])
                # col_name: time
                st.text(f'Prep Time: {0} seconds')
                # col_name: calories
                st.text(f'Calories: {0} calories')
                # col_name: cuisine
                st.text(f'Cuisine: {0}')
                # col_name: rating
                st.text(f'Rating: {0}')
            # response will return recipes
    #         print(query_string)
    #         recipeId int NOT NULL AUTO_INCREMENT,
    # name varchar(255) NOT NULL,
    # cuisine varchar(30) NOT NULL,
    # calories int NOT NULL,
    # time int NOT NULL,
    # instructions varchar(2000) NOT NULL, -- May need to increase size
    # image varchar(2500) NOT NULL,
    # PRIMARY KEY(recipeId),
    # CONSTRAINT UC_recipe_name UNIQUE(name)
            
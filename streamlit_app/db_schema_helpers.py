import streamlit as st
from PIL import Image
import random
import db
from queries import *

# This function is used to output each of the recipe cards given a db response of a recipe table resp.
# add_index is a boolean flag if we want to have some sort of order mentioned on the card (eg. most popular recipes in order).
def rec_table_to_posts(resp, add_index=False):
    user_signed_in = st.session_state['logged_in']
    for c, item in enumerate(resp):
            image_container, description_container = st.columns([2, 2])
            with image_container:
                # col_name: image
                # change this later.. need to fetch the file first
                image = Image.open('coconut.jpeg')
                new_image = image.resize((600, 400))
                st.image(new_image)
            with description_container:
                # col_name: name
                if add_index:
                    st.text(f'#{c + 1}. {item[1]}')
                else:
                    st.text(item[1])
                # col_name: time
                st.text(f'Prep Time: {item[4]} minutes')
                # col_name: calories
                st.text(f'Calories: {item[3]} calories')
                # col_name: cuisine
                st.text(f'Cuisine: {item[2].title()}')
                # col_name: rating
                # query the rating of the recipe since it is in a different table
                check_rating = recipe_id_to_rating.format(item[0])
                res = db.query(check_rating)
                if res == []:
                    st.text('Number of Ratings: Not Rated Yet, be the first!')
                else:
                    st.text(f'Number of Ratings: {res[0][0]}')
                # IF a user has signed in, provide them functionality to edit ratings.
                if user_signed_in:
                    with st.form('Rate' + str(c)):
                        number = st.number_input('Rate 1-5', min_value=1, max_value=5, value=5)
                        submitted = st.form_submit_button("Rate")
                        if submitted:
                            query_string = user_add_rating.format(st.session_state['user_obj']['id'], item[0], number, number)
                            print(query_string)
                            db.query(query_string, insert=True)
                            st.write("Thanks for your rating!")
                            st.experimental_rerun()
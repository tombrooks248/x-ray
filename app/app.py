#-------------------------------------------------------------------------------
# Libraries
#-------------------------------------------------------------------------------
import streamlit as st
import numpy as np
import pandas as pd
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_image_select import image_select
from PIL import Image
from sklearn.preprocessing import MinMaxScaler

#Local functions
#-------------------------------------------------------------------------------
from x_ray_model import x_ray_classifier



#Tab Title
#-------------------------------------------------------------------------------
st.set_page_config(
    page_title="X-Ray Analyser",
    page_icon="🚑",
)


#On page Title and Logo
#-------------------------------------------------------------------------------

image = Image.open('x-ray-logo.jpeg')

col1, col2 = st.columns(2)
with col1:
    st.write('')

    st.write('')

    st.markdown("<h1 style='text-align: center; color: white;'>X-Ray Analyzer</h1>", unsafe_allow_html=True)

with col2:
    st.image(image, width=150)

#with col3:
#    st.write(' ')
st.markdown("---")

## importing images before selection
image = Image.open("../data/web_test/NORMAL/IM-0075-0001.jpeg")



#Form for selecting X-Ray image to check
#-------------------------------------------------------------------------------
image_options=[
        Image.open("../data/web_test/PNEUMONIA/person40_virus_87.jpeg"),
        Image.open("../data/web_test/PNEUMONIA/person24_virus_58.jpeg"),
        Image.open("../data/web_test/NORMAL/IM-0079-0001.jpeg"),
        Image.open("../data/web_test/NORMAL/IM-0077-0001.jpeg"),
    ]


search_input = ""

with st.form("select_box_form"):
   img = image_select(
    label="Select a X-Ray",
    images=image_options,
    captions=["Pneumonia 1", "Pnumonia 2", "Normal 1", "Normal 2"],
    #return_value="index"
    )

   # Every form must have a submit button.
   submitted = st.form_submit_button("Analyze Image")
   if submitted:
       search_input = img




#or import your own image
#-------------------------------------------------------------------------------




with st.form("user_upload_form"):

    uploaded_file = st.file_uploader("Choose your own image", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Analze Image")
    if submitted:
       search_input = image


if (search_input):
    prediction = x_ray_classifier(search_input)[0][0]

    st.markdown("#### The chances of your X-Ray *showing Pneumonia* are:")

    #scaler = MinMaxScaler(data_min)

    prediction = prediction*10000
    prediction = np.log(prediction)
    prediction = prediction/10

    prediction = prediction +0.5
    if prediction > 1:
        prediction = 0.999


    if prediction < 0.5:
        st.markdown('#### '+ ':green['+str(round(prediction*100,2))+'%]')
        st.markdown('#### Your X-Ray :green[is probably clear] 👍')
    else:
        st.markdown('#### '+ ':red['+str(round(prediction*100,2))+'%]')
        st.markdown('#### Your X-Ray indicates :red[you have Pnumonia]. 😔')

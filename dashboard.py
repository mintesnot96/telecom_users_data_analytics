import pandas as pd
import numpy
import streamlit as st
import os
import pickle
from sklearn.preprocessing import StandardScaler
from PIL import Image
# setting path to file and folders
user_df= pd.read_csv("./data/teleco_user_sat_data.csv")

st.title("What is your customer's satisfaction level?")
st.subheader("This model will predict the satisfaction score of a user")

model = pickle.load(open("./models/pridict_satisfaction_model.sav", 'rb'))
#result = loaded_model.score(x_test, y_test)
#result

xdr = st.number_input("xDr_session_count")
tot = st.number_input("Total Data Volume")
dur = st.number_input("Total Session Duration")
rtt = st.number_input("Average RTT")
tp = st.number_input("Average Throughput")
tcp = st.number_input("TCP volume")

input_data = [xdr , tot, dur , rtt, tp, tcp]
prediction = model.predict([input_data])

st.subheader("The satisfaction score is: {}".format ( prediction))

st.subheader("The Dataset")

st.write(
  user_df
)

st.subheader("Applications Data Usage")
image = Image.open('./image/applications.jpg')
st.image(image, caption='scatter plot of applications and total data volume')

st.subheader("Top 3 Handset Manufacturers")
image2 = Image.open('./image/top3.png')
st.image(image2, caption='Top 3 Handset Manufacturers')

st.subheader("Top 10 Handset Types")
image3 = Image.open('./image/top10.png')
st.image(image3, caption='Top 10 Handset Types')

st.subheader("Engagement metrics Distribution")
image4 = Image.open('./image/totdist.png')
st.image(image4, caption='Distribution of engagement matrics: xdr, total data volume, session duration')

st.subheader("Experience metrics Distribution")
image5 = Image.open('./image/rttdist.png')
st.image(image5, caption='Distribution of experience matrics: RTT, TP, TCP')
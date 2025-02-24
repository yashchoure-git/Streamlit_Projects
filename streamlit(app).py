import streamlit as st
import pickle
import numpy as np
import time as t

model_path="C:\\Users\\DELL\\Downloads\\stock_price_prediction.pkl"
model=pickle.load(open(model_path,"rb"))



st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSB2i3TRjUdc-FHVaQGw6C8b0OQHB2cF5bLbQ&s")

st.title("Stock Price Prediction📊 ")

st.markdown("____________________________________________________________________________________________________________")

st.info("Note:Input Stocks info correctly")

stock_name=st.text_input("Enter Stock Name")

Open_Price=st.number_input("Enter Open Price",min_value=0.0)
High_Price=st.number_input("Enter High Price",min_value=0.0)
Low_Price=st.number_input("Enter Low Price ",min_value=0.0)
Trading_Volume=st.number_input("Enter Trading Volume")

if st.button("Predict Price"):
   
   with st.spinner("Predicting"):
        t.sleep(4)
   
   inputs=np.array([Open_Price,High_Price,Low_Price,Trading_Volume]).reshape(1,-1)

   predicted_price=model.predict(inputs)[0]
   
   st.success(f"Stock-:{stock_name}")
   st.success(f"Predicted Price:{predicted_price}INR")
   st.line_chart(inputs)
   
st.sidebar.image("https://www.logomaker.com/api/main/images/1j_ojFVGOMkX9W_reBe4hGfa1qnF7kJamhmOzFo_OWhfqQ1hhnx00v9t9fQ...KBsE4VUdw01bf8Yr1nE8XIEDyUQ8vnrYNIpEX359xikNXu0RTS9rIEG4T6HC6kc4w7Epxtcd90...GUiSmQkbYc9o_MI7aw7hmBJxkhm...GJDchon95V...VJKczNTJIgnpGuU...pN6UDHF95RIOo-")

st.sidebar.text_input("Enter E-mail")
st.sidebar.text_input("Enter Password")
st.sidebar.button("Create account")

feedback=st.sidebar.slider("Rate your experience!(1-5)",1,5)
if st.sidebar.button("Summit"):
    st.sidebar.success(f"Thanks for giving us {feedback} stars!")   


  
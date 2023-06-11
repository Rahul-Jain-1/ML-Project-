
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler
from PIL import Image

import streamlit as st

@st.cache
def process_input_text(input_text):
    # Perform data processing or computations based on the input text
    # Return the processed result

    input_text = st.text_input("Enter text", "")
    processed_result = process_input_text(input_text)

    # Use the processed result in your app
    st.write("Processed Result:", processed_result)

  
# loading in the model to predict on the data
pickle_in = open('EEG Eye State Classification\content\model.pkl', 'rb')
classifier = pickle.load(pickle_in)
scaler = pickle.load(open('EEG Eye State Classification\content\scaler.pkl', 'rb'))
  
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(AF3,F7,F3,FC5,T7,P7,O1,O2,P8,T8,FC6,F4,F8,AF4):  
   
   features = [AF3,F7,F3,FC5,T7,P7,O1,O2,P8,T8,FC6,F4,F8,AF4]
   scaledfeatures = scaler.transform([features])
   prediction1 = classifier.predict(scaledfeatures)
    #4335.9,3991.28,4277.44,4142.05,4331.79,4610.26,4070.26,4609.74,4202.05,4238.46,4192.31,4296.92,4638.46,4414.36
   print(prediction1)
    
   if(prediction1 == 0):
       return "closed. "
    
   else:
        return "open. "
    
    
      
def show_main_page():
    st.title("EEG Eye State Prediction")
    st.write("The EEG Eye State Classification project is a machine learning application that aims to predict the eye state of an individual based on their electroencephalogram (EEG) data. EEG is a technique used to record electrical activity in the brain by placing electrodes on the scalp. By analyzing the EEG signals, it is possible to infer the state of the individual's eyes, whether they are open or closed.")
    st.write("The project involves developing a machine learning model that can accurately classify the eye state based on the EEG data. This typically involves several steps, including data preprocessing, feature extraction, and model training. The EEG signals are preprocessed to remove noise and artifacts, and relevant features are extracted to represent the data. Various machine learning algorithms, such as support vector machines (SVM), random forests, or deep learning models, can be used to train the classifier.")

    st.write("The trained model is then deployed in a user-friendly interface using Streamlit, a popular Python library for building interactive web applications. The interface allows users to upload their EEG data or provide real-time data through appropriate sensors. The EEG signals are processed by the model, and the predicted eye state (open or closed) is displayed to the user.")

    st.write("The EEG Eye State Classification project has various applications in areas such as healthcare, human-computer interaction, and neurology. It can be used to monitor drowsiness or alertness levels in drivers, detect sleep disorders, or enable hands-free control in assistive technologies.")

    st.write("By accurately predicting the eye state from EEG signals, this project showcases the potential of machine learning techniques in analyzing brain activity and provides a practical tool for eye state classification based on EEG data.")
  
# this is the main function in which we define our webpage 
def show_another_page():
    #st.title("EEG Eye State Prediction")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:black;padding:13px">
    <h2 style ="color:black;text-align:center;">Streamlit Eye State Classifier ML App </h2>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)

    st.markdown("\n\n")
    # st.markdown(
    # """
    # <style>
    # input.textInput {{
    #     width: 10px;
    #     height: 30px;
    #     font-size: 14px;
    #     padding: 5px;
    #     box-sizing: border-box;
    # }}
    # </style>
    # """,    unsafe_allow_html=True
    # )   
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    AF3 = st.text_input("AF3 Value", "Text-here", key="AF3")
    F7 = st.text_input("F7 Value", key="F7")
    F3 = st.text_input("F3 Value", key="F3")
    FC5 = st.text_input("FC5 Value", key="FC5")
    T7 = st.text_input("T7 Value", key="T7")
    P7 = st.text_input("P7 Value", key="P7")
    O1 = st.text_input("O1 Value", key="O1")
    O2 = st.text_input("O2 Value", key="O2")
    P8 = st.text_input("P8 Value", key="P8")
    T8 = st.text_input("T8 Value", key="T8")
    FC6 = st.text_input("FC6 Value", key="FC6")
    F4 = st.text_input("F4 Value", key="F4")
    F8 = st.text_input("F8 Value", key="F8")
    AF4 = st.text_input("AF4 Value", key="AF4")

    # sepal_length = st.text_input("Sepal Length", "Type Here")
    # sepal_width = st.text_input("Sepal Width", "Type Here")
    # petal_length = st.text_input("Petal Length", "Type Here")
    # petal_width = st.text_input("Petal Width", "Type Here")
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(AF3,F7,F3,FC5,T7,P7,O1,O2,P8,T8,FC6,F4,F8,AF4)
    st.success('Eyes is {}'.format(result))
     
def app():
    st.title("EEG EYE STATE CLASSIFIER")

    # Create a sidebar menu for page navigation
    menu = ["Introduction", "Real-time Eye State Prediction"]
    choice = st.sidebar.selectbox("Select App", menu)

    if choice == "Introduction":
        show_main_page()
    elif choice == "Real-time Eye State Prediction":
        show_another_page()

if __name__ == '__main__':
    app()

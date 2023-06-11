import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My WebPage",page_icon=":tada:",layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    #load assets 
    lottie_coding = "https://assets1.lottiefiles.com/packages/lf20_0yfsb3a1.json"


    #header
    with st.container():
        st.subheader("Hi I am Rahul Jain")
        st.title("A student from GGSIPU")
        st.write("I am passoiniate about working with real time ml models. ")
        st.write("[Learn More?](https://www.kaggle.com/search?q=face+and+eye)")

    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What i do ")
            st.write("##")
            st.write(
                """

                """
            )
            st.write("[Utine channel](https://www.youtube.com/watch?v=VqgUkExPvLY)")

        with right_column:
            st_lottie(lottie_coding,height=300,key='coding ')    

        # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        # with image_column:
        #     st.image(img_lottie_animation)
        with text_column:
            st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
            st.write(
                """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
                In this tutorial, I'll show you exactly how to do it
                """
            )
            
            st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
            
    with st.container():
        image_column, text_column = st.columns((1, 2))
        # with image_column:
        #     st.image(img_contact_form)
        with text_column:
            st.subheader("How To Add A Contact Form To Your Streamlit App")
            st.write(
                """
                Want to add a contact form to your Streamlit website?
                In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
                """
            )
            st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")        

if __name__ == "__main__":
    app()
import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
st.set_page_config(page_title="My WebPage",page_icon=":tada:",layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_7VEmrT02fx.json")
lottie_content = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lt8ter7g.json")
image = Image.open('content/an-electroencephalogram-or-eeg-being-performed-image-credit-baburov-2009.jpg')

def local_csv(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>(f.read())</style>",unsafe_allow_html=True)
local_csv("content/style.css")

def app():
    st.write("##")
    st.subheader("Hey Guys :wave:")
    st.title("My Portfolio Website ")
    st.write("""
        I am gonna explain briefly about how streamlit can be used to build interactive and responsibe website to deploy any Machine learning model. 
    """)
    st.write("[Read More](https://streamlit.io/)")
    st.write("---")
    
    with st.container():
        selected = option_menu(
            menu_title = None,
            options = ['About','Projects','Contacts'],
            icons = ['person','code-slash','chat-left-text-fill'],
            orientation = 'horizontal' 
        )
    if selected =='About':
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.write("##")
                st.subheader("I am Rahul Jain")
                st.title("Undergrad at USAR")
            with col2:
                st_lottie(lottie_coder)
            st.write("---")
    
            with st.container():
                col3,col4= st.columns(2)     
                with col3:
                    st.subheader("""
                    Education
                    - GGSIPU 
                        - Bachelor of Engineering - Artifical Intelligence and Data Science
                        - CGPA - 9.5 (overall) 
                    - Preet Public Sr Sec School 
                        - PCM
                        - Percentage - 90%
    
                    """)
                with col4:
                    st.subheader("""
                    Experience 
                    - GirlScript Summer of Code 
                        -  Duration - 3 months    
                        - Remote 
                    """)    
    
    if selected == 'Projects':
        with st.container():
            st.header("My Projects ")
            st.write("##")
            col5,col6 = st.columns((1,2))
            with col5 :
                st.image(image)
            with col6 :
                st.subheader("EEG Eye State Classification")
                st.write("""
                EEG eye state classification begins with the collection of EEG data using specialized electrodes placed on the scalp to measure the electrical activity in the brain. Simultaneously, eye state labels are recorded, typically through manual observation or eye-tracking devices. The collected EEG data undergoes preprocessing steps to remove noise, artifacts, and baseline drift, ensuring the data is clean and suitable for analysis. EEG Eye State Classification refers to the task of analyzing electroencephalogram (EEG) data collected from the human brain to determine the current state of the eyes, whether they are open or closed
                """)
                st.markdown("[Visit Github Repository](https://github.com/Rahul-Jain-1/ML-project-Eye-State-Classification)")
    
    if selected == 'Contacts':
        st.header("Get In Touch ")
        st.write("##")
        st.write("##")
        contact_form = """"
        <div class="form-container">
            <form action="https://formsubmit.co/your@email.com" method="POST">
            <input type="text" name="name" placeholder="Name" required>
            <input type="email" name="email" placeholder="Email" required>
            <input type="text" name="subject" placeholder="Subject" required>
            <textarea name="message" placeholder="Message" rows="5" required></textarea>
            <button type="submit">Send</button>
            </form>
        </div>
        """
        left_col, right_col = st.columns((2,1))
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st_lottie(lottie_content,height=300)
    # #load assets 
    # lottie_coding = "https://assets1.lottiefiles.com/packages/lf20_0yfsb3a1.json"


    # #header
    # with st.container():
    #     st.subheader("Hi I am Rahul Jain")
    #     st.title("A student from GGSIPU")
    #     st.write("I am passoiniate about working with real time ml models. ")
    #     st.write("[Learn More?](https://www.kaggle.com/search?q=face+and+eye)")

    # with st.container():
    #     st.write("---")
    #     left_column, right_column = st.columns(2)
    #     with left_column:
    #         st.header("What i do ")
    #         st.write("##")
    #         st.write(
    #             """

    #             """
    #         )
    #         st.write("[Utine channel](https://www.youtube.com/watch?v=VqgUkExPvLY)")

    #     with right_column:
    #         st_lottie(lottie_coding,height=300,key='coding ')    

    #     # ---- PROJECTS ----
    # with st.container():
    #     st.write("---")
    #     st.header("My Projects")
    #     st.write("##")
    #     image_column, text_column = st.columns((1, 2))
    #     # with image_column:
    #     #     st.image(img_lottie_animation)
    #     with text_column:
    #         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
    #         st.write(
    #             """
    #             Learn how to use Lottie Files in Streamlit!
    #             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
    #             In this tutorial, I'll show you exactly how to do it
    #             """
    #         )
            
    #         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
            
    # with st.container():
    #     image_column, text_column = st.columns((1, 2))
    #     # with image_column:
    #     #     st.image(img_contact_form)
    #     with text_column:
    #         st.subheader("How To Add A Contact Form To Your Streamlit App")
    #         st.write(
    #             """
    #             Want to add a contact form to your Streamlit website?
    #             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
    #             """
    #         )
    #         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")        

if __name__ == "__main__":
    app()

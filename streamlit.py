import streamlit as st
import os
def UI():
    st.set_page_config(
        page_title="PDF_GENERATOR",
        page_icon="🤖",
    )
    
    st.write('develop11')

    st.write(os.getcwd())

if __name__ == "__main__":
    UI()

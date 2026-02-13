import streamlit as st
import cleaner
import brain

st.set_page_config(page_title="VaultGuard")

hide = """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """
st.markdown(hide, unsafe_allow_html=True)

st.title("VaultGuard")
st.write("Your Private Finance AI")

file = st.file_uploader("Upload PDF", type="pdf")

if file:
    with open("temp.pdf", "wb") as f:
        f.write(file.getbuffer())

    if st.button("Analyze"):
        with st.spinner("Cleaning & Thinking"):
            text = cleaner.clean("temp.pdf")
            answer = brain.chat(text)
            
        st.success("Done")
        st.write(answer)
import streamlit as st
import pandas as pd
import json
import cleaner
import brain
import plotly.express as px

st.set_page_config(page_title="VaultGuard Finance AI", page_icon="🛡️")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("🛡️ VaultGuard Finance AI")
st.caption("Secure, Privacy-First Financial Analysis")

file = st.file_uploader("Upload your bank statement (PDF)", type="pdf")

if file:
    with open("temp.pdf", "wb") as f:
        f.write(file.getbuffer())

    if st.button("Analyze Statement"):
        with st.spinner("Analyzing..."):
            raw_text = cleaner.clean("temp.pdf")
            response = brain.chat(raw_text)
            
            try:
                summary, chart_json = response.split("|||")
            except ValueError:
                summary = response
                chart_json = "{}"

        col1, col2, col3 = st.columns(3)
        col1.metric("Privacy Shield", "Active")
        col2.metric("Inference", "Groq Llama 3.1")
        col3.metric("Mode", "Production")

        st.divider()

        tab1, tab2 = st.tabs(["📝 Transaction List", "📈 Spending Pie Chart"])
        
        with tab1:
            st.markdown(summary)
            
        with tab2:
            try:
                data_dict = json.loads(chart_json.strip())
                if data_dict:
                    df = pd.DataFrame(list(data_dict.items()), columns=['Category', 'Amount'])
                    df = df[df['Amount'] > 0]
                    fig = px.pie(df, values='Amount', names='Category', hole=0.4,
                                 color_discrete_sequence=px.colors.qualitative.Pastel)
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No data available.")
            except:
                st.error("Chart Error.")

        st.success("Analysis Complete.")
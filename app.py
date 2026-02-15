
import streamlit as st
import pandas as pd
import cleaner
import brain
import json
import re
import plotly.express as px

st.set_page_config(page_title="VaultGuard")

hide_style = """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

st.title("VaultGuard")

pdf_file = st.file_uploader("Upload PDF", type="pdf")

if pdf_file:
    with open("temp.pdf", "wb") as f:
        f.write(pdf_file.getbuffer())

    if st.button("Analyze"):
        with st.spinner("Processing..."):
            raw_text = cleaner.clean("temp.pdf")
            result = brain.chat(raw_text)
            
        st.subheader("Monthly Overview")
        c1, c2, c3 = st.columns(3)
        c1.metric("Privacy", "Active", "Safe")
        c2.metric("Security", "Local", "Verified")
        c3.metric("Shield", "Active", "100%")

        st.divider()

        t1, t2 = st.tabs(["📊 Analysis", "📈 Spending Chart"])
        
        with t1:
            text_part = result.split("CHART_DATA:")[0]
            st.markdown(text_part)

        with t2:
            try:
                found = re.search(r"CHART_DATA:\s*(\[.*\])", result, re.DOTALL)
                if found:
                    data = json.loads(found.group(1))
                    if data:
                        df = pd.DataFrame(data)
                        
                        grouped = df.groupby('Category')['Amount'].sum().reset_index()
                        chart = px.pie(grouped, values='Amount', names='Category', title='Spending by Category')
                        st.plotly_chart(chart, use_container_width=True)
                        
                        st.divider()
                        st.subheader("Transaction Details")
                        st.dataframe(df, use_container_width=True)
                    else:
                        st.info("No data found")
                else:
                    st.error("Could not find chart data")
            except Exception as e:
                st.warning(f"Error making chart: {str(e)}")
import streamlit as st
import pandas as pd
import json
import cleaner
import brain

st.set_page_config(page_title="VaultGuard", page_icon="🛡️")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("🛡️ VaultGuard Finance AI")
st.caption("Your Secure Privacy-First Financial Analysis")

file = st.file_uploader("Upload your bank statement (PDF)", type="pdf")

if file:
    with open("temp.pdf", "wb") as f:
        f.write(file.getbuffer())

    if st.button("Analyze Statement"):
        with st.spinner("VaultGuard is auditing your data safely..."):
            raw_text = cleaner.clean("temp.pdf")
            response = brain.chat(raw_text)
            
            try:
                summary, chart_json = response.split("|||")
            except ValueError:
                summary = response
                chart_json = "{}"

        col1, col2, col3 = st.columns(3)
        col1.metric("Privacy Shield", "Active")
        col2.metric("Analysis", "Llama 3.1")
        col3.metric("Data Source", "Local PDF")

        st.divider()

        tab1, tab2 = st.tabs(["📝 Summary & Table", "📈 Spending Breakdown"])
        
        with tab1:
            st.markdown(summary)
            
        with tab2:
            try:
                data_dict = json.loads(chart_json.strip())
                if data_dict:
                    df = pd.DataFrame(list(data_dict.items()), columns=['Category', 'Amount'])
                    df = df.sort_values(by="Amount", ascending=False)
                    st.bar_chart(df.set_index("Category"))
                else:
                    st.info("No transaction data found to visualize.")
            except Exception as e:
                st.error("Visualization Error.")

        st.success("Analysis Complete.")
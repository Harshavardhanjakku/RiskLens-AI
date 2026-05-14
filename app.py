import streamlit as st
import requests

st.set_page_config(
    page_title="AI TPRM Assistant",
    layout="wide"
)

st.title("AI-Powered TPRM Evidence Review Assistant")

uploaded_files = st.file_uploader(
    "Upload Security Evidence",
    accept_multiple_files=True,
    type=["pdf", "docx", "xlsx"]
)

if uploaded_files:

    for uploaded_file in uploaded_files:

        st.write(f"Uploaded: {uploaded_file.name}")

        with st.spinner(f"Analyzing {uploaded_file.name}..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type
                )
            }

            response = requests.post(
                "https://risklens-ai-go8b.onrender.com/analyze",
                files=files
            )

            st.write("Status Code:", response.status_code)

            try:

                data = response.json()

                if "error" in data:

                    st.error(data["error"])

                else:

                    st.success("Assessment Completed")

                    st.json(data["analysis"])

            except Exception as e:

                st.error("JSON Decode Error")

                st.text(response.text)
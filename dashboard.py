import streamlit as st
import requests

st.set_page_config(page_title="GenAI ContentOps", layout="wide")

st.title("🚀 GenAI ContentOps Dashboard")

# Input
topic = st.text_input("Enter Topic")

if st.button("Run Pipeline"):
    if topic:
        with st.spinner("Running AI pipeline..."):
            response = requests.post(
                "http://127.0.0.1:8000/run-pipeline",
                json={"topic": topic}
            )

            data = response.json()

        st.success("Pipeline executed successfully!")

        # Draft
        st.subheader("📝 Draft Content")
        st.write(data["draft"]["content"])

        # Compliance
        st.subheader("🔍 Compliance")
        st.write(f"Status: {data['compliance']['status']}")

        # Localization
        st.subheader("🌐 Localization")
        st.write("**English:**", data["localization"]["english"])
        st.write("**Hindi:**", data["localization"]["hindi"])
        st.write("**Hinglish:**", data["localization"]["hinglish"])

        # Distribution
        st.subheader("📡 Distribution")
        st.write(data["distribution"]["status"])

        # Intelligence
        st.subheader("🧠 Intelligence")
        st.write("CTR:", data["intelligence"]["CTR"])
        st.write("Engagement:", data["intelligence"]["engagement"])

    else:
        st.warning("Please enter a topic")
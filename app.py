# app.py

import streamlit as st
import re
from generator import execute_automation_cycle

st.set_page_config(page_title="AI Site Factory", page_icon="🚀", layout="centered")

st.title("🚀 Autonomous Website Factory")
st.markdown("Enter a website description below. This dashboard will cleanly spin up a standalone repository, commit code structure, and host it via GitHub Pages.")

with st.form("automator_form"):
    user_prompt = st.text_area("Describe your website intent:", placeholder="e.g., A clean menu page for a local cafe...")
    repo_input = st.text_input("Repository Name:", placeholder="e.g., dynamic-cafe-shop")
    submitted = st.form_submit_button("Generate & Publish Live")

if submitted:
    if not user_prompt.strip() or not repo_input.strip():
        st.error("❌ Both the descriptive prompt and tracking repository path name are required parameters.")
    else:
        clean_name = re.sub(r'[^a-zA-Z0-9\-]', '', repo_input.lower().replace(' ', '-'))
        progress = st.progress(0, text="Initializing core pipelines...")
        
        try:
            progress.progress(30, text="🔨 Provisioning fresh GitHub target repositories...")
            progress.progress(60, text="🎨 Processing rules engine templates and writing files...")
            
            live_site_url = execute_automation_cycle(user_prompt.strip(), clean_name)
            
            progress.progress(100, text="🎉 Workspace synchronized successfully!")
            st.success("🏆 Operations completed without anomalies!")
            
            # Accessing username directly from the native stream registry layout
            username = st.secrets["GITHUB_USERNAME"]
            col1, col2 = st.columns(2)
            with col1:
                st.link_button("📂 View Source Code", f"https://github.com/{username}/{clean_name}")
            with col2:
                st.link_button("🌐 Open Live Website", live_site_url)
        except Exception as e:
            progress.empty()
            st.error(f"❌ Automation runtime failure: {str(e)}")

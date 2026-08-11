# generator.py

import os
import time
import base64
import requests
import streamlit as st
from components import route_prompt_to_template

def create_github_repo(repo_name):
    """Provisions a clean public repository directly using API request methods."""
    token = st.secrets["GITHUB_TOKEN"].replace('"', '').replace("'", "").strip()
    username = st.secrets["GITHUB_USERNAME"].replace('"', '').replace("'", "").strip()
    
    url = "https://github.com"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    data = {"name": repo_name, "auto_init": True, "private": False}
    
    response = requests.post(url, json=data, headers=headers)
    
    # 201 = Created, 422 = Repository already exists on this account profile
    if response.status_code in [201, 422]:
        return True
        
    raise Exception(f"GitHub Repository Creation Failed. Code: {response.status_code} | Reason: {response.reason}")

def upload_index_html(repo_name, html_content):
    """Bypasses local GitPython files completely by writing index.html using web requests."""
    token = st.secrets["GITHUB_TOKEN"].replace('"', '').replace("'", "").strip()
    username = st.secrets["GITHUB_USERNAME"].replace('"', '').replace("'", "").strip()
    
    url = f"https://github.com{username}/{repo_name}/contents/index.html"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    
    # Base64 encode the HTML data string as mandated by GitHub's raw Content APIs
    encoded_content = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")
    
    # Check if index.html already exists to handle dynamic update loops
    check_response = requests.get(url, headers=headers)
    sha = None
    if check_response.status_code == 200:
        sha = check_response.json()["sha"]
        
    data = {
        "message": "feat: autonomous dynamic system layout compilation via cloud automation",
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha # Attach historical tracking hash if modifying an existing asset
        
    response = requests.put(url, json=data, headers=headers)
    if response.status_code in [200, 201]:
        return True
        
    raise Exception(f"File injection failed. Code: {response.status_code} | Reason: {response.reason}")

def enable_github_pages(repo_name):
    """Triggers GitHub REST endpoints to provision active public web routing."""
    token = st.secrets["GITHUB_TOKEN"].replace('"', '').replace("'", "").strip()
    username = st.secrets["GITHUB_USERNAME"].replace('"', '').replace("'", "").strip()
    
    url = f"https://github.com{username}/{repo_name}/pages"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    data = {"source": {"branch": "main", "path": "/"}}
    
    # Give the GitHub remote indexing loop a moment to register our content upload
    time.sleep(4)  
    
    for _ in range(3):
        response = requests.post(url, json=data, headers=headers)
        if response.status_code in [201, 409]: # 201 = Created, 409 = Pages already active
            return f"https://{username}.github.io/{repo_name}/"
        time.sleep(4)
        
    return f"https://{username}.github.io/{repo_name}/"

def execute_automation_cycle(prompt, repo_name):
    """Orchestrates purely cloud-native site creation loops without hard drive requirements."""
    # 1. Spawn repository infrastructure online
    create_github_repo(repo_name)
    
    # 2. Compile prompt metadata rules using our dynamic component router
    html_payload = route_prompt_to_template(prompt)
    
    # 3. Direct write content upstream using rapid web APIs
    upload_index_html(repo_name, html_payload)
        
    # 4. Provision deployment servers
    return enable_github_pages(repo_name)

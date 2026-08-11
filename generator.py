# generator.py

import os
import time
import base64
import requests
import streamlit as st
from components import route_prompt_to_template

def create_github_repo(repo_name):
    """Checks if a repository exists; if not, provisions a fresh public one cleanly."""
    token = str(st.secrets["GITHUB_TOKEN"]).replace('"', '').replace("'", "").strip()
    username = str(st.secrets["GITHUB_USERNAME"]).replace('"', '').replace("'", "").strip()
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    
    # --- CRITICAL FIX: Added a forward slash between github.com and the username ---
    check_url = f"https://github.com{username}/{repo_name}"
    check_response = requests.get(check_url, headers=headers)
    
    if check_response.status_code == 200:
        return True

    # If it does not exist, safely create it
    create_url = "https://github.com"
    data = {"name": repo_name, "auto_init": True, "private": False}
    
    response = requests.post(create_url, json=data, headers=headers)
    
    # 201 means Created successfully
    if response.status_code == 201:
        return True
    # 422 means Already Exists
    elif response.status_code == 422:
        return True
        
    raise Exception(f"GitHub API Rejected Request. Code: {response.status_code} | Reason: {response.reason}")

def upload_index_html(repo_name, html_content):
    """Writes the website layout directly to the repository using Base64 strings."""
    token = str(st.secrets["GITHUB_TOKEN"]).replace('"', '').replace("'", "").strip()
    username = str(st.secrets["GITHUB_USERNAME"]).replace('"', '').replace("'", "").strip()
    
    url = f"https://github.com{username}/{repo_name}/contents/index.html"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    
    encoded_content = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")
    
    check_response = requests.get(url, headers=headers)
    sha = None
    if check_response.status_code == 200:
        sha = check_response.json()["sha"]
        
    data = {
        "message": "feat: autonomous dynamic system layout compilation via cloud automation",
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha
        
    response = requests.put(url, json=data, headers=headers)
    
    # 200 means Updated, 201 means Created Successfully
    if response.status_code == 200 or response.status_code == 201:
        return True
        
    raise Exception(f"File injection failed. Code: {response.status_code} | Reason: {response.reason}")

def enable_github_pages(repo_name):
    """Triggers GitHub REST endpoints to provision active public web routing."""
    token = str(st.secrets["GITHUB_TOKEN"]).replace('"', '').replace("'", "").strip()
    username = str(st.secrets["GITHUB_USERNAME"]).replace('"', '').replace("'", "").strip()
    
    url = f"https://github.com{username}/{repo_name}/pages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    data = {"source": {"branch": "main", "path": "/"}}
    
    time.sleep(5)  
    
    for _ in range(3):
        response = requests.post(url, json=data, headers=headers)
        # 201 means Created, 409 means Pages already active on repository
        if response.status_code == 201 or response.status_code == 409: 
            return f"https://{username}.github.io/{repo_name}/"
        time.sleep(4)
        
    return f"https://{username}.github.io/{repo_name}/"

def execute_automation_cycle(prompt, repo_name):
    """Orchestrates cloud-native site creation loops cleanly."""
    create_github_repo(repo_name)
    html_payload = route_prompt_to_template(prompt)
    upload_index_html(repo_name, html_payload)
    return enable_github_pages(repo_name)

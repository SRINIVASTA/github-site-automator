# generator.py

import os
import time
import base64
import requests
import streamlit as st
from components import route_prompt_to_template

def create_github_repo(repo_name):
    """Provisions a clean public repository using clean Basic Auth headers."""
    # Squeeze out hidden quotation mark strings or structural whitespaces
    token = str(st.secrets["GITHUB_TOKEN"]).replace('"', '').replace("'", "").strip()
    username = str(st.secrets["GITHUB_USERNAME"]).replace('"', '').replace("'", "").strip()
    
    url = "https://github.com"
    
    # Bypasses Bearer parsing anomalies by passing username and token via Basic Auth
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    
    data = {"name": repo_name, "auto_init": True, "private": False}
    
    # Pass token safely using the auth parameter tuple matrix
    response = requests.post(url, json=data, headers=headers, auth=(username, token))
    
    # 201 = Created, 422 = Repository already exists on your profile account
    if response.status_code in [201, 422]:
        return True
        
    raise Exception(f"GitHub Repository Creation Failed. Code: {response.status_code} | Reason: {response.reason}")

def upload_index_html(repo_name, html_content):
    """Writes the website layout directly to the new repository via web strings."""
    token = str(st.secrets["GITHUB_TOKEN"]).replace('"', '').replace("'", "").strip()
    username = str(st.secrets["GITHUB_USERNAME"]).replace('"', '').replace("'", "").strip()
    
    url = f"https://github.com{username}/{repo_name}/contents/index.html"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    
    encoded_content = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")
    
    check_response = requests.get(url, headers=headers, auth=(username, token))
    sha = None
    if check_response.status_code == 200:
        sha = check_response.json()["sha"]
        
    data = {
        "message": "制造: autonomous dynamic system layout compilation",
        "content": encoded_content
    }
    if sha:
        data["sha"] = sha
        
    response = requests.put(url, json=data, headers=headers, auth=(username, token))
    if response.status_code in [200, 201]:
        return True
        
    raise Exception(f"File injection failed. Code: {response.status_code} | Reason: {response.reason}")

def enable_github_pages(repo_name):
    """Triggers GitHub REST endpoints to provision active public web routing."""
    token = str(st.secrets["GITHUB_TOKEN"]).replace('"', '').replace("'", "").strip()
    username = str(st.secrets["GITHUB_USERNAME"]).replace('"', '').replace("'", "").strip()
    
    url = f"https://github.com{username}/{repo_name}/pages"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    data = {"source": {"branch": "main", "path": "/"}}
    
    time.sleep(6)  
    
    for _ in range(3):
        response = requests.post(url, json=data, headers=headers, auth=(username, token))
        if response.status_code in [201, 409]:
            return f"https://{username}.github.io/{repo_name}/"
        time.sleep(4)
        
    return f"https://{username}.github.io/{repo_name}/"

def execute_automation_cycle(prompt, repo_name):
    """Orchestrates purely cloud-native site creation loops without hard drive requirements."""
    create_github_repo(repo_name)
    html_payload = route_prompt_to_template(prompt)
    upload_index_html(repo_name, html_payload)
    return enable_github_pages(repo_name)

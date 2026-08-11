# generator.py

import os
import time
import requests
import streamlit as st  # Imported to access st.secrets natively
from git import Repo
from components import route_prompt_to_template

# Grab keys directly from Streamlit's unified secure tracking context dict
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
GITHUB_USERNAME = st.secrets["GITHUB_USERNAME"]

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_github_repo(repo_name):
    url = "https://github.com"
    data = {"name": repo_name, "auto_init": True, "private": False}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        return response.json()["clone_url"]
    elif response.status_code == 422:
        return f"https://github.com/{GITHUB_USERNAME}/{repo_name}.git"
    return None

def enable_github_pages(repo_name):
    url = f"https://github.com{GITHUB_USERNAME}/{repo_name}/pages"
    data = {"source": {"branch": "main", "path": "/"}}
    time.sleep(6)  # Safety pause for internal GitHub synchronization
    
    for _ in range(3):
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            return response.json()["html_url"]
        time.sleep(4)
    return f"https://{GITHUB_USERNAME}.github.io/{repo_name}/"

def execute_automation_cycle(prompt, repo_name):
    clone_url = create_github_repo(repo_name)
    if not clone_url:
        raise Exception("Failed to provision GitHub repository infrastructure.")
        
    auth_url = clone_url.replace("https://", f"https://{GITHUB_TOKEN}@")
    base_dir = os.path.join(os.getcwd(), "generated_sites")
    os.makedirs(base_dir, exist_ok=True)
    local_dir = os.path.join(base_dir, repo_name)
    
    if not os.path.exists(local_dir):
        repo = Repo.clone_from(auth_url, local_dir)
    else:
        repo = Repo(local_dir)
        repo.remotes.origin.pull()

    html_payload = route_prompt_to_template(prompt)
    with open(os.path.join(local_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_payload)
        
    repo.index.add(["index.html"])
    if repo.is_dirty():
        repo.index.commit("feat: autonomous dynamic system layout compilation")
        repo.remote(name='origin').push()
        
    return enable_github_pages(repo_name)

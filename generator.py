# generator.py

import os
import time
import requests
import streamlit as st
from git import Repo
from components import route_prompt_to_template

def create_github_repo(repo_name):
    """Programs a fresh repository structure using active Streamlit session credentials."""
    # Pull secrets inside execution layer to prevent blank initialization states
    token = st.secrets["GITHUB_TOKEN"]
    username = st.secrets["GITHUB_USERNAME"]
    
    url = "https://github.com"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app" # Satisfies GitHub firewall requirements
    }
    data = {"name": repo_name, "auto_init": True, "private": False}
    
    response = requests.post(url, json=data, headers=headers)
    
    # 201 = Created Successfully, 422 = Repo Name Already Exists on Account
    if response.status_code == 201:
        return response.json()["clone_url"]
    elif response.status_code == 422:
        print(f"⚠️ Repo '{repo_name}' detected on remote cluster. Syncing tracking nodes...")
        return f"https://github.com{username}/{repo_name}.git"
    
    # Trace specific permission blocks
    raise Exception(f"GitHub API Rejected Request. Code: {response.status_code} | Reason: {response.text}")

def enable_github_pages(repo_name):
    """Triggers GitHub REST endpoints to provision active public web routing."""
    token = st.secrets["GITHUB_TOKEN"]
    username = st.secrets["GITHUB_USERNAME"]
    
    url = f"https://github.com{username}/{repo_name}/pages"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    data = {"source": {"branch": "main", "path": "/"}}
    
    # Give the GitHub remote indexing loop 6 seconds to register initial file commits
    time.sleep(6)  
    
    # Fail-safe structural retry loop
    for _ in range(3):
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            return response.json()["html_url"]
        time.sleep(4)
        
    return f"https://{username}.github.io/{repo_name}/"

def execute_automation_cycle(prompt, repo_name):
    """Orchestrates structural building loops, git pushing, and cloud deployments."""
    token = st.secrets["GITHUB_TOKEN"]
    
    # 1. Run the repository builder with enhanced error trapping
    clone_url = create_github_repo(repo_name)
        
    auth_url = clone_url.replace("https://", f"https://{token}@")
    base_dir = os.path.join(os.getcwd(), "generated_sites")
    os.makedirs(base_dir, exist_ok=True)
    local_dir = os.path.join(base_dir, repo_name)
    
    # 2. Synchronize workspace code directories
    if not os.path.exists(local_dir):
        repo = Repo.clone_from(auth_url, local_dir)
    else:
        repo = Repo(local_dir)
        repo.remotes.origin.pull()

    # 3. Compile prompt metadata rules
    html_payload = route_prompt_to_template(prompt)
    with open(os.path.join(local_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_payload)
        
    # 4. Fire updates upstream to remote origin paths
    repo.index.add(["index.html"])
    if repo.is_dirty():
        repo.index.commit("feat: autonomous dynamic system layout compilation")
        repo.remote(name='origin').push()
        
    # 5. Provision deployment servers
    return enable_github_pages(repo_name)

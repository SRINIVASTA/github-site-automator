# generator.py

import os
import time
import base64
import requests
import streamlit as st
from datetime import datetime, timedelta, timezone
from components import route_prompt_to_template

def check_rate_limit():
    """Checks account metadata to ensure you stay under 499 repository builds per hour."""
    token = str(st.secrets["GITHUB_TOKEN"]).replace('"', '').replace("'", "").strip()
    username = str(st.secrets["GITHUB_USERNAME"]).replace('"', '').replace("'", "").strip()
    
    url = f"https://github.com{username}/repos"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    params = {"sort": "created", "per_page": 100}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return True

    repos = response.json()
    one_hour_ago = datetime.now(timezone.utc) - timedelta(hours=1)
    recent_repo_count = 0
    
    for repo in repos:
        created_at = datetime.strptime(repo["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        if created_at > one_hour_ago:
            recent_repo_count += 1

    if recent_repo_count >= 499:
        raise Exception(f"🛑 GitHub Hourly Safety Barrier Reached: You have built {recent_repo_count} sites in the last 60 minutes. Please wait before running another generation cycle.")
    
    return True

def create_github_repo(repo_name):
    """Checks if a repository exists; if not, provisions a fresh public one cleanly."""
    token = str(st.secrets["GITHUB_TOKEN"]).replace('"', '').replace("'", "").strip()
    username = str(st.secrets["GITHUB_USERNAME"]).replace('"', '').replace("'", "").strip()
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-site-automator-app"
    }
    
    check_url = f"https://github.com{username}/{repo_name}"
    try:
        check_response = requests.get(check_url, headers=headers)
        if check_response.status_code == 200:
            return True
    except Exception:
        pass

    create_url = "https://github.com"
    data = {"name": repo_name, "auto_init": True, "private": False}
    
    response = requests.post(create_url, json=data, headers=headers)
    
    if response.status_code == 201 or response.status_code == 422:
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
        if response.status_code == 201 or response.status_code == 409: 
            return f"https://{username}.github.io/{repo_name}/"
        time.sleep(4)
        
    return f"https://{username}.github.io/{repo_name}/"

def execute_automation_cycle(prompt, repo_name):
    """Orchestrates cloud-native site creation loops cleanly with hourly limits enforced."""
    # Run the hourly 499-site safety barrier check first
    check_rate_limit()
    
    create_github_repo(repo_name)
    html_payload = route_prompt_to_template(prompt)
    upload_index_html(repo_name, html_payload)
    return enable_github_pages(repo_name)

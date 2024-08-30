import sys
import os
import subprocess

from langchain.tools import tool

@tool('push_to_github', return_direct=False)
def push_to_github(repo_url: str) -> str:
    """Push files from the current directory to the specified GitHub repository."""
    try:
        # Initialize git
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Automated commit'], check=True)
        subprocess.run(['git', 'remote', 'add', 'origin', repo_url], check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'master'], check=True)
        return 'Files pushed to GitHub successfully.'
    except Exception as e:
        return f'Error: {str(e)}'
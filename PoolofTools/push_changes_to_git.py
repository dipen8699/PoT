from langchain.tools import tool
import subprocess

@tool
def push_changes():
    """Pushes current changes to the current Git branch."""
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True)
        # Commit changes
        subprocess.run(['git', 'commit', '-m', 'Automated commit'], check=True)
        # Push changes to the current branch
        subprocess.run(['git', 'push'], check=True)
        return 'Changes pushed successfully!'
    except subprocess.CalledProcessError as e:
        return f'An error occurred: {e}'
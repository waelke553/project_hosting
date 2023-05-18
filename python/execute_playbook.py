import os
import subprocess

def execute_playbook(playbook_path, extra_vars=None):
    # Change to the directory containing the playbook
    playbook_directory = os.path.dirname(playbook_path)
    os.chdir(playbook_directory)

    # Construct the ansible-playbook command
    command = ['ansible-playbook', playbook_path]
    if extra_vars:
        command.extend(['-e', extra_vars])

    # Execute the ansible-playbook command
    subprocess.run(command, check=True)

# Example usage
playbook_path = '/home/wael/project_hosting/ansible-playbook/playbook.yaml'
extra_vars = "varA=okey varB=newValue"
execute_playbook(playbook_path, extra_vars)

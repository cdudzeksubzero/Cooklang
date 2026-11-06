import paramiko
from pathlib import Path

hostname = "pikitchen.local"
remote_file_path = "/home/kitchen/Cooklang/recipes/.shopping-list"

## Auth: Use password or key_filename
username = "kitchen"
# password = "your_password"
key_filename=Path.home() / ".ssh" / "id_ed25519"

# Establish SSH Connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, key_filename=str(key_filename.absolute()))

# Open SFTP session and read the file
try:
    sftp = ssh.open_sftp()
    with sftp.open(remote_file_path, "r") as remote_file:
        content = remote_file.read().decode("utf-8")

    print()
    print(content)
except Exception as e:
    print(f"Error reading remote file: {e}")
finally:
    sftp.close()
    ssh.close()

from ftplib import FTP_TLS
import os
from mimetypes import guess_type, add_type


# Function to open an FTP_TLS connection
def open_connection(server, user, pwd, work_dir=None):
    try:
        ftps = FTP_TLS(host=server)
        ftps.login(user=user, passwd=pwd)
        ftps.prot_p()  # Switch to secure data connection
        if work_dir is not None:
            ftps.cwd(work_dir)
        return ftps
    except Exception as e:
        print(f"Error: {e}")
        return None


# Function to download a file from the FTP server
def download_file(ftps, remote_path, local_path):
    remote_file = os.path.basename(remote_path)
    local_file_path = os.path.join(local_path, remote_file)

    # Differentiate between text and binary files
    file_type, encoding = guess_type_and_encoding(remote_file)

    try:
        if file_type.split("/")[0] == "text" and encoding is None:
            # Use text mode for transfer
            local_file = open(local_file_path, "w")

            def callback(line):
                local_file.write(line + "\n")

            ftps.retrlines("RETR " + remote_file, callback)
            local_file.close()
        else:
            # Use binary mode for transfer
            local_file = open(local_file_path, "wb")
            ftps.retrbinary("RETR " + remote_file, local_file.write)
            local_file.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


# Function to guess the file type and encoding
def guess_type_and_encoding(filename):
    add_type("text/x-python-win", ".pyw")  # Not in tables
    mimetype, encoding = guess_type(filename, False)  # Allow extras
    mimetype = mimetype or "?/?"  # Type unknown
    return mimetype, encoding


# Define FTP server parameters
server = "172.20.10.2 "
user = "santos"
pwd = "santos2023"
work_dir = (
    "/Users/user/Desktop/ftpserver"  # Change this to the desired remote directory
)

# Create an FTP_TLS connection
ftps = open_connection(server, user, pwd, work_dir)

if ftps is not None:
    # Specify the remote and local file paths for download
    remote_file_path = "/Users/user/Desktop/ftpserver/example.txt"
    local_download_dir = "/Users/user/Desktop/ftpserver"

    # Download the file
    if download_file(ftps, remote_file_path, local_download_dir):
        print("File downloaded successfully")
    else:
        print("File download failed")

    # Close the FTP connection
    ftps.quit()

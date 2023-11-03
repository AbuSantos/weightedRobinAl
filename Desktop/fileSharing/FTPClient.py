# from ftplib import FTP

# # Define FTP server parameters
# FTP_HOST = "127.0.0.1"
# FTP_PORT = 2121
# FTP_USER = "destiny"
# FTP_PASSWORD = "destiny2023"

# # Create an FTP client session
# ftp = FTP()

# # Connect to the FTP server
# ftp.connect(FTP_HOST, FTP_PORT)

# # Login with the provided credentials
# ftp.login(user=FTP_USER, passwd=FTP_PASSWORD)

# # Change to the directory where you want to upload the file on the server
# remote_directory = "ftpclient"  # Replace with the desired directory on the server
# ftp.cwd(remote_directory)

# # Specify the name of the file on the server
# remote_file_name = "example.docx"

# # Specify the local file to be uploaded
# # local_file_path = "/Users/user/Desktop/ftpserver/ftpclient/example.docx"  # Replace with the correct local file path
# local_file_path = "/Users/user/Desktop/ftpserver/ftpdownload/example.docx"  # Replace with the correct local file path

# # Upload the local file to the server
# with open(local_file_path, "rb") as local_file:
#     ftp.storbinary(f"STOR {remote_file_name}", local_file)
#     print("Upload completed")


# # # Download the file from the server
# with open(local_file_path, "wb") as local_file:
#     ftp.retrbinary(f"RETR {remote_file_name}", local_file.write)
#     print("Download completed")

# # Logout and close the connection
# ftp.quit()


from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import threading

# Define FTP server parameters
FTP_HOST = "127.0.0.1"
FTP_PORT = 2121
FTP_USER = "destiny"
FTP_PASSWORD = "destiny2023"

# Create an authorizer with a callback for custom error handling
class CustomAuthorizer(DummyAuthorizer):
    def on_login(self, username):
        # Implement custom error handling for login, if needed
        pass

    def on_login_failed(self, username):
        # Implement custom error handling for failed login, if needed
        pass

authorizer = CustomAuthorizer()
authorizer.add_user(FTP_USER, FTP_PASSWORD, "/Users/user/Desktop/ftpserver", perm="elradfmw")

# Create a custom FTP handler with error handling
class CustomFTPHandler(FTPHandler):
    def on_login_failed(self, username):
        # Log login failures or implement custom error handling
        pass

# Create the FTP server with multi-threading support
def run_ftp_server():
    handler = CustomFTPHandler
    handler.authorizer = authorizer
    server = FTPServer((FTP_HOST, FTP_PORT), handler)

    print(f"FTP Server listening on {FTP_HOST}:{FTP_PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("FTP Server terminated.")

if __name__ == "__main__":
    ftp_server_thread = threading.Thread(target=run_ftp_server)

    # Start the FTP server in a separate thread
    ftp_server_thread.start()
    ftp_server_thread.join()

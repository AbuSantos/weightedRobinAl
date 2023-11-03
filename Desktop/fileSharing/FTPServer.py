from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define FTP server parameters
FTP_HOST = "127.0.0.1"
FTP_PORT = 2121
FTP_USER = "destiny"
FTP_PASSWORD = "destiny2023"

# Create an authorizer
authorizer = DummyAuthorizer()
authorizer.add_user(
    FTP_USER, FTP_PASSWORD, "/Users/user/Desktop/ftpserver", perm="elradfmw"
)

# Create an FTP handler with the authorizer
handler = FTPHandler
handler.authorizer = authorizer

# Create the FTP server
server = FTPServer((FTP_HOST, FTP_PORT), handler)

print(f"FTP Server listening on {FTP_HOST}:{FTP_PORT}")
server.serve_forever()

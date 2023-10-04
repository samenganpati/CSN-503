import os
import socket
from tqdm import tqdm
from getpass import getuser

IP = socket.gethostbyname(socket.gethostname())
PORT = 44560
ADDR = (IP, PORT)
print(ADDR)
SIZE = 1024
FORMAT = "ISO-8859-1"
FILENAME = "book.pdf"
FILESIZE = os.path.getsize(FILENAME)

def main():
    """ TCP socket and connecting to the server """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    """ Sending the filename and filesize to the server. """
    with open(FILENAME,"rb") as f:
        data = f.read()
    
    client.sendall(FILENAME.encode(FORMAT))
    client.sendall(str(FILESIZE).encode(FORMAT))
    client.sendall(data)
    client.send(b"<END>")
    client.close()

if __name__ == "__main__":
    main()
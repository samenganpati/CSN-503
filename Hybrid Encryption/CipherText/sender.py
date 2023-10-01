import os
import socket
from tqdm import tqdm
from getpass import getuser

IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
print(ADDR)
SIZE = 1024
FORMAT = "ISO-8859-1"
FILENAME = "book.pdf.enc"
FILESIZE = os.path.getsize(FILENAME)

def main():
    """ TCP socket and connecting to the server """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    """ Sending the filename and filesize to the server. """
    data = f"{FILENAME}_{FILESIZE}"
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"SERVER: {msg}")

    """ Data transfer. """
    bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(FILENAME, "r" ,encoding="ISO-8859-1") as f:
        while True:
            data = f.read(SIZE)

            if not data:
                break

            client.send(data.encode(FORMAT))
            msg = client.recv(SIZE).decode(FORMAT)

            bar.update(len(data))

    """ Closing the connection """
    client.close()

if __name__ == "__main__":
    main()
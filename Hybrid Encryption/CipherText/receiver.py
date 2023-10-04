
import socket
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 44560
ADDR = (IP, PORT)
print(ADDR)
SIZE = 1024
FORMAT = "ISO-8859-1"

def main():
    """ Creating a TCP server socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[+] Listening...")

    """ Accepting the connection from the client. """
    conn, addr = server.accept()
    print(f"[+] Client connected from {addr[0]}:{addr[1]}")

    """ Receiving the filename and filesize from the client. """
    FILENAME = conn.recv(SIZE).decode(FORMAT)
    FILESIZE = conn.recv(SIZE).decode(FORMAT)
    print("file name : " , FILENAME)
    print("file size : " , FILESIZE)


    file = open("rev_book.pdf","wb")
    done = False
    file_bytes = b""

    """ Data transfer """
    bar = tqdm(unit="B", unit_scale=True, unit_divisor=1000,total=int(FILESIZE))

    while not done:
        data = conn.recv(SIZE)

        if file_bytes[-5:] == b"<END>":
            done = True
        else:
            file_bytes += data
        bar.update(SIZE)
    file.write(file_bytes[:-5])

    """ Closing connection. """
    conn.close()
    server.close()

if __name__ == "__main__":
    main()

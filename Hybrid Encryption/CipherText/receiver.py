
import socket
from tqdm import tqdm

IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
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
    data = conn.recv(SIZE).decode(FORMAT)
    item = data.split("_")
    FILENAME = item[0]
    FILESIZE = int(item[1])

    print("[+] Filename and filesize received from the client.")
    conn.send("Filename and filesize received".encode(FORMAT))

    """ Data transfer """
    bar = tqdm(range(FILESIZE), f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(f"recv_{FILENAME}", "w",encoding="ISO-8859-1") as f:
        while True:
            data = conn.recv(SIZE).decode(FORMAT)

            if not data:
                break

            f.write(data)
            conn.send("Data received.".encode(FORMAT))

            bar.update(len(data))

    """ Closing connection. """
    conn.close()
    server.close()

if __name__ == "__main__":
    main()

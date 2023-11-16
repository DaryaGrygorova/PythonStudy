"""Task 2 - Echo server with multiprocessing
Create a socket echo server that handles each connection
using the multiprocessing library.
"""
import multiprocessing
import os
import socket

HOST = "127.0.0.1"
PORT = 65432


def connection_handler(connection):
    """Connection handler. Receive the data and retransmit it
    Close connection after client session ends.
    """
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(f"Received data: {data.decode('utf-8')}, process: {os.getpid()}")
        print("Sending data back to the client")
        connection.sendall(data)
    connection.close()


def run_server():
    """Run echo-server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print(f"Starting up on {HOST}:{PORT}")

        while True:
            print("Waiting for a connection...")
            connection, address = sock.accept()
            print(f"Accepted address: {address}")

            process = multiprocessing.Process(target=connection_handler, args=(connection,))

            process.start()
            process.join()
            print(f"Client session ended!!! Address: {address}")


if __name__ == "__main__":
    run_server()

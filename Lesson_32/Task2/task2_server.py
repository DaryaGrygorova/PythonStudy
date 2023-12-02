"""Echo server, which returns to client the data,
encrypted using the Caesar cipher algorithm by a specific key
obtained from the client."""
import json
import socket

HOST = "127.0.0.1"  # Standard loop-back interface address (localhost)
PORT = 65432

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
print(f"starting up on {HOST} port {PORT}")
sock.bind((HOST, PORT))

# Listen for incoming connections
sock.listen(1)


def caesar_encryption(string: str, shift: int):
    """Returns string, encrypted using the Caesar cipher algorithm"""
    encoded_str = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                encoded_str += chr((ord(char) + shift - ord("A")) % 26 + ord("A"))
            else:
                encoded_str += chr((ord(char) + shift - ord("a")) % 26 + ord("a"))
        else:
            encoded_str += char
    return encoded_str


# assert caesarEncryption('ABC abc, XYZ xyz', 3) == 'DEF def, ABC abc'


while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                print(f"Received data: {data}")
                data_json = json.loads(data.decode("utf-8"))
                message = data_json.get("message")
                key = data_json.get("key")

                print("Sending data back to the client")
                res_data = caesar_encryption(message, key).encode("utf-8")
                connection.sendall(res_data)

            else:
                print("No data from", client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

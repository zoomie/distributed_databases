import socket
import sys


def set_value(key, value):
    with open(key, 'w') as file:
        json.dump(value, file)

    with open("data2/history.puff", "a") as file:
        row = key + '----' + str(value)
        file.write(row)
        file.write('\n')


def get_value(key):
    with open(key, 'r') as file:
        data = json.load(file)
    return data

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        input_data = str()
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                connection.sendall(data)
                input_data += str(data)
            else:
                break
        key, value = input_data.split('----')
        print(key, value)
    finally:
        connection.close()

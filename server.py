import socket
import sys

# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global sock
        host = ""
        port = 9999
        sock = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))
        
# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global sock
        print("Binding socket to port: " + str(port))
        sock.bind((host, port))
        sock.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg)+ "\n"+ "Retrying....")
        socket_bind()

# Establish a connection with client (socket must be listening)
def socket_accept():
    conn, addr = sock.accept()
    print("Connection has been established | " +"IP "+ addr[0]+ "| port "+str(addr[1]))
    send_commands(conn)
    conn.close()

# Send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            sock.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

if __name__ == "__main__":
    main()
            



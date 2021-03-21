"""
Server IP is 52.88.20.156, ports are 5000-5008, socket is UNIX TCP 
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
"""
import socket

def main():

    PORT_ADDRESS = 8080
    HOST = '137.135.87.94'
    
    # TODO: Create a socket and connect it to the server at the designated IP and port
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT_ADDRESS))

    # TODO: Get user input and send it to the server using your TCP socket

        user_input = input()
        s.sendall(user_input.encode('utf-8'))

    # TODO: Receive a response from the server and close the TCP connection

        response = s.recv(1024)
        print(response)
        s.close()

if __name__ == '__main__':
    main()

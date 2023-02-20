import os

serverApp = "server.py"
clientApp = "client.py"

def StartFile():
    os.startfile(serverApp)
    os.startfile(clientApp)
    exit()
StartFile()

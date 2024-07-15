import socket
def run_client():
    try:
        #create a socket object for the client
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server running on localhust at port 3333
        client.connect(("localhost", 3333))
        while True:
            #recieve a message from the server
            message = client.recv(1024).decode()
            if not message:
                break #Exit the loop if no message is recieved
            #Prompt the user for inout on the server message and send the response
            client.send(input(message).encode())
            response = client.recv(1024).decode()
            print(response)
    except Exception as e:
        #print any error that occurs during the connection or communication
        print(f"An error ocurred: {e}")
    finally:
        #ensure the client socket is closed
        client.close()
#if the script is run directly, execute the run_client function
if __name__ == "__main__":
    run_client()





















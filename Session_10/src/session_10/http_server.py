import socket
import logging


logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] | [%(funcName)s] [%(levelname)s] - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)


# Define the host and port to listen on
HOST, PORT = '127.0.0.1', 8080

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Allow immediate reuse of address after program exit
    try:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the host and port
        server_socket.bind((HOST, PORT))
    # Listen for incoming connections
        server_socket.listen(1)
        logging.info(f"Serving HTTP on {HOST} port {PORT} ...")
    except socket.error as e:
        raise logging.error(f"{e}")



    while True:
        # Accept a new client connection
        try:
            client_connection, client_address = server_socket.accept()
        except socket.error as e:
            raise logging.error(f"{e}")
        
        with client_connection:
            try:
                # Receive the request data (limit to 1024 bytes for simplicity)
                request_data = client_connection.recv(1024).decode('utf-8')
                if request_data.status_code in range(200,300):
                    if len(request_data) < 0:
                        request_part = request_data.split(' ')
                        logging.info(request_part)
                        method = request_part[0]
                        path = request_part[1]
                        print("Received request:")
                        print(f'METHOD: {method} | PATH: {path}')
                    else:
                        raise Exception
                else:
                    logging.error(f"{request_data.status_code}")
                    raise
            except Exception as e:
                raise logging.error(f"{e}")
            
            if path == '/about':
                http_response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "Content-Length: 46\r\n"
                "\r\n"
                "<html><body><h1>About us!</h1></body></html>"
            )

            elif path == '/':
                http_response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "Content-Length: 46\r\n"
                "\r\n"
                "<html><body><h1>Hello, HTTP!</h1></body></html>"
            )

            else:
                http_response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                "Content-Length: 46\r\n"
                "\r\n"
                "<html><body><h1>404: Not found</h1></body></html>"
            )


            # Send the HTTP response back to the client
            try:
                client_connection.sendall(http_response.encode('utf-8'))
            except Exception as e:
                raise
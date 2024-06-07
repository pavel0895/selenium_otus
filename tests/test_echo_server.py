import socket
from http import HTTPStatus

HOST = '127.0.0.1'
PORT = 8080


def parse_request(request):
    lines = request.decode().splitlines()
    method, path, _ = lines[0].split()
    headers = {}
    for line in lines[1:]:
        if line:
            key, value = line.split(":", 1)
            headers[key.strip()] = value.strip()

    status_code = 200
    if "?" in path:
        _, query_string = path.split("?", 1)
        params = dict(p.split("=") for p in query_string.split("&"))
        if "status" in params:
            try:
                status_code = int(params["status"])
            except ValueError:
                pass

    return method, headers, status_code


def generate_response(method, headers, status_code, client_address):
    status_phrase = HTTPStatus(status_code).phrase
    response = f"HTTP/1.1 {status_code} {status_phrase}\r\n"
    response += "Content-Type: text/plain\r\n"
    response += "\r\n"
    response += f"Request Method: {method}\r\n"
    response += f"Request Source: {client_address}\r\n"
    response += f"Response Status: {status_code} {status_phrase}\r\n"
    for key, value in headers.items():
        response += f"{key}: {value}\r\n"
    return response.encode()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер запущен на http://{HOST}:{PORT}/")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Подключено к: {client_address}")
            request = client_socket.recv(1024)
            if request:
                method, headers, status_code = parse_request(request)
                response = generate_response(method, headers, status_code, client_address)
                client_socket.sendall(response)

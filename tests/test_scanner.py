import socket
import threading
import time

from opscan.scanner import check_port


def test_check_port():
    def listen_port(addr, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((addr, port))
        sock.listen()

        while True:
            try:
                connection, address = sock.accept()
                connection.close()
            except KeyboardInterrupt:
                break

    addr = "localhost"
    port = 8888

    listener = threading.Thread(
        target=listen_port, args=(addr, port), daemon=True
    )
    listener.start()

    # Ensure daemon thread is running
    time.sleep(1)

    result = check_port(addr, port)
    assert result is True

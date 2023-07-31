import socket
from concurrent import futures
from typing import List

from rich import print


def check_port(addr: str, port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((addr, port))
    sock.close()

    return result == 0


def resolve_ip(host: str) -> str:
    return socket.gethostbyname(host)


class Scanner:
    def __init__(
        self, addrs: List[str], min_port: int, max_port: int, concurrent: int
    ) -> None:
        self.addrs = addrs
        self.min_port = min_port
        self.max_port = max_port
        self.concurrent = concurrent

    def run(self) -> None:
        with futures.ThreadPoolExecutor(
            max_workers=self.concurrent
        ) as executor:
            futures_ = {}
            for addr in self.addrs:
                ipaddr = resolve_ip(addr)
                for port in range(self.min_port, self.max_port + 1):
                    future = executor.submit(check_port, ipaddr, port)
                    futures_[future] = (addr, port)

            for future in futures.as_completed(futures_):
                addr, port = futures_[future]
                if future.result() is True:
                    print(f"{addr}:{port} ✅")

from typing import List

import typer
from typing_extensions import Annotated

from .scanner import Scanner

app = typer.Typer()


@app.command()
def main(
    addrs: List[str],
    port: Annotated[int, typer.Option(help="Ports to be scanned")] = None,
    concurrent: Annotated[
        int, typer.Option(help="Number of concurrent port scanning")
    ] = 10,
):
    if port:
        min_port = max_port = port
    else:
        min_port = 0
        max_port = 65535

    s = Scanner(addrs, min_port, max_port, concurrent)
    s.run()

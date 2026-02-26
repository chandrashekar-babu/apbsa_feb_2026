import trio
import itertools

import logging
import logging.config

CONNECTION_COUNTER = itertools.count()

logging.basicConfig(filename="/tmp/simple_tcp_server_trio.log", 
                    level=logging.DEBUG,
                    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s"
)

async def echo_server(server_stream):
    ident = next(CONNECTION_COUNTER)
    print(f"echo_server {ident}: started")
    try:
        async for data in server_stream:
            print(f"echo_server {ident}: received data {data!r}")
            await server_stream.send_all(data)
        print(f"echo_server {ident}: connection closed")
    except Exception as exc:
        print(f"echo_server {ident}: crashed: {exc!r}")

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()

    parser.add_argument("--port", type=int, default=9876)
    args = parser.parse_args()

    trio.run(trio.serve_tcp, echo_server, args.port)

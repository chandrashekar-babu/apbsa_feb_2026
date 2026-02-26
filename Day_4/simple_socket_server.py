from socket import socket, AF_INET, SOCK_STREAM, SOMAXCONN, SHUT_RD, SOL_SOCKET, SO_REUSEADDR, SO_REUSEPORT
import logging
import logging.config

#logging.config.fileConfig("simple_socket_server_logging.ini")
logging.basicConfig(filename="simple_socket_server.log", 
                    level=logging.DEBUG,
                    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s"
)

log = logging.getLogger(__name__)

hostname, port = "localhost", 9876


def echo_handler(conn, addrinfo):
    log = logging.getLogger("echo_handler")
    log.info(f"Handling client connection from {addrinfo}")

    ins, outs = conn.makefile("r"), conn.makefile("w")
    while True:
        line = ins.readline()
        log.debug(f"Got message from {addrinfo}: {line.strip()}")

        if "exit" in line:
            log.debug(f"Got an 'exit' message from {addrinfo}") 
            break
        outs.write(line.upper())
        outs.flush()

    log.info(f"Closing connection for {addrinfo}")
    ins.close()
    outs.close()


if __name__ == '__main__':
    log.info("Creating a new socket")

    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)


        log.debug(f"Binding socket to {hostname}:{port}")
        sock.bind((hostname, port))
        log.debug("Setting up the listen queue...")
        sock.listen(SOMAXCONN)

        log.info("Waiting for incoming connections...")
        client, addrinfo = sock.accept()
        log.info(f"Got incoming connection from {client=}, {addrinfo=}")

        echo_handler(client, addrinfo)
        client.close()

    finally:
        sock.shutdown(SHUT_RD)

    


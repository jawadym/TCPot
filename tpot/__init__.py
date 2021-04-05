from datetime import datetime
import logging
import threading
from socket import socket, timeout


class TCPot():
    def __init__(self, bind, ports, log_file_path):
        self.now = datetime.now()
        self.bind = bind
        try:
            self.ports = [int(port) for port in ports.split(",")]
            if len(ports) < 1:
                raise Exception(f"""
                Error going through specified ports
                """)
        except ValueError as V_ERR:
            print(f"""
            Failed to parse ports 
            {V_ERR}
            Exiting ...
            """)
            sys.exit(-1)

        self.log_file_path = log_file_path
        self.listener_threads = {}
        self.msg = "2320 Cannot connect to Host"
        self.logger = self.logger_start()
        self.logger.info(
            f'{self.now.strftime("%H:%M:%S")} - {self.__class__.__name__} initialized...')
        self.logger.info(
            f'{self.now.strftime("%H:%M:%S")} - PORTS: {":".join([str(port) for port in self.ports])}')

    def listen(self):
        for port in self.ports:
            self.listener_threads[port] = threading.Thread(
                target=self.start_listener_thread, args=(port,))
            self.listener_threads[port].start()

    def start_listener_thread(self, port):
        listener = socket()
        listener.bind((self.bind, port))
        listener.listen(5)
        while True:
            client, addr = listener.accept()
            client_handler = threading.Thread(
                target=self.handle, args=(client, port, addr[0], addr[1]))
            client_handler.start()

    def handle(self, client, port, ip, remote_port):
        current = self.now.strftime("%H:%M:%S")
        self.logger.info(
            f'{current} - Connection received: {ip}:{remote_port} => {port}')

        client.settimeout(4)
        try:
            data = client.recv(64)
            current = self.now.strftime("%H:%M:%S")
            self.logger.info(
                f"{current} - Data received: {remote_port}:{ip} => {port}: {data}")
            client.send(self.msg.encode("utf8"))
            current = self.now.strftime("%H:%M:%S")
            self.logger.info(f"{current} - Sent {self.msg}")
        except timeout:
            pass
        client.close()

    def logger_start(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%s',
                            filename=self.log_file_path,
                            filemode='w')
        logger_instance = logging.getLogger(__name__)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        logger_instance.addHandler(console_handler)
        return logger_instance

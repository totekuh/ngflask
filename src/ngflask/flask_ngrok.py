#!/usr/bin/env python3
import os

from flask import Flask
from flask_autoindex import AutoIndex
from pyngrok import ngrok

DEFAULT_IP = "127.0.0.1"
DEFAULT_PORT = 4200
DEFAULT_DIRECTORY = os.getcwd()


def get_arguments():
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Flask/Ngrok HTTP Server')
    parser.add_argument('-i',
                        "--ip",
                        dest="ip",
                        required=False,
                        default=DEFAULT_IP,
                        type=str,
                        help="The local IP address to bind to. "
                             f"Default is {DEFAULT_IP}.")
    parser.add_argument('-p',
                        "--port",
                        dest="port",
                        required=False,
                        default=DEFAULT_PORT,
                        type=str,
                        help="The local TCP port to bind to. "
                             f"Default is {DEFAULT_PORT}.")
    parser.add_argument('-d',
                        "--directory",
                        dest="directory",
                        required=False,
                        default=DEFAULT_DIRECTORY,
                        type=str,
                        help="The local directory to shave over the ngrok network. "
                             "Default is the current working directory.")
    parser.add_argument('-pf',
                        '--print-files',
                        dest='print_files',
                        action='store_true',
                        required=False,
                        help="Specify if the script should print URLs to files found in the shared directory "
                             "for them to be copy-pasted. "
                             "By default the script doesn't print them.")
    options = parser.parse_args()
    return options


class TunneledHttpServer:
    def __init__(self, ip: str, port: int, directory: str, print_files: bool = False):
        self.ip = ip
        self.port = port
        self.directory = directory
        self.print_files = print_files

        self.app = Flask(__name__)
        AutoIndex(self.app, browse_root=self.directory)

    def start(self):
        self.app.config.from_mapping(
            BASE_URL=f"http://{self.ip}:{self.port}",
            USE_NGROK=True
        )
        self.public_url = ngrok.connect(self.port, bind_tls=True).public_url
        print(f" * Ngrok tunnel {self.public_url} -> http://{self.ip}:{self.port}/")
        print(f" * Serving files from the '{self.directory}' directory")

        if self.print_files:
            for current_path, folders, files in os.walk(self.directory):
                for file in files:
                    relpath = os.path.relpath(os.path.join(current_path, file))
                    relpath = relpath.replace(f'..{os.linesep}', '').replace(f"{self.directory[1:]}", '')
                    print(f" * Serving '{self.public_url}/{relpath}'")
        else:
            print(f" * Hint: use -pf or --print-files for printing URLs for all the files shared over ngflask")
        self.app.config["BASE_URL"] = self.public_url
        self.app.run(host=self.ip, port=self.port)


def main():
    options = get_arguments()
    tunneled_http_server = TunneledHttpServer(ip=options.ip,
                                              port=options.port,
                                              directory=options.directory,
                                              print_files=options.print_files)
    tunneled_http_server.start()

if __name__ == '__main__':
    main()
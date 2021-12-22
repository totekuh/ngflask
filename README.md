# ngflask
Serving static files and directories from your local machine over the Internet with just one command.

The script first binds a flask server to the given address and starts sharing files from the specified directory.

It then creates a tunnel through the Ngrok network and gives you the public URL tunneled to the local flask server.

Useful for transferring the files when you compromised a host inside an internal network and outgoing Internet connections aren't forbidden.

## Installation

```bash
sudo apt install python3 python3-pip
git clone https://github.com/cyberhexe/ngflask
cd ngflask
pip3 install -r requirements.txt
sudo link flask-ngrok.py /usr/bin/ngflask
```

Or using PyPI
```bash
pip3 install ngflask
```

## Usage

### Serve files and folder from the current working directory
`ngflask`

### Serve files and folders from the /tmp directory
`ngflask --directory /tmp`

### Print served files to the console on startup
`ngflask --directory /tmp -pf`

### Bind the server to a specific address
`ngflask --ip 10.10.10.10 --port 5050`

### Print help
`ngflask -h`
